#!/usr/bin/env python3
"""Generate machine-readable engagement state from human-readable Markdown sources."""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGAGEMENT = ROOT / "engagement"
CONFIG = ROOT / "config"
PLANS = ROOT / "plans"


def clean(value: str) -> str:
    return value.replace("`", "").strip()


def key_name(value: str) -> str:
    value = value.lower().replace("/", "_")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def markdown_tables(path: Path) -> list[list[dict[str, str]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    tables: list[list[dict[str, str]]] = []
    index = 0
    while index < len(lines) - 1:
        if not (lines[index].strip().startswith("|") and lines[index + 1].strip().startswith("|")):
            index += 1
            continue
        header = [clean(part) for part in lines[index].strip().strip("|").split("|")]
        separator = [part.strip() for part in lines[index + 1].strip().strip("|").split("|")]
        if not header or not all(set(part) <= {"-", ":", " "} for part in separator):
            index += 1
            continue
        rows: list[dict[str, str]] = []
        index += 2
        while index < len(lines) and lines[index].strip().startswith("|"):
            values = [clean(part) for part in lines[index].strip().strip("|").split("|")]
            if len(values) == len(header):
                rows.append({key_name(header[pos]): values[pos] for pos in range(len(header))})
            index += 1
        tables.append(rows)
    return tables


def all_table_rows(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for table in markdown_tables(path):
        rows.extend(table)
    return rows


def engagement_fields() -> dict[str, str]:
    fields: dict[str, str] = {}
    for row in all_table_rows(ENGAGEMENT / "Engagement-Info.md"):
        if "field" in row and "value" in row:
            fields[key_name(row["field"])] = clean(row["value"])
    for raw in (ENGAGEMENT / "Engagement-Info.md").read_text(encoding="utf-8").splitlines():
        match = re.match(r"^-\s+([^:]+):\s*(.+)$", raw.strip())
        if match:
            fields[key_name(match.group(1))] = clean(match.group(2))
    return fields


def list_value(value: str) -> list[str]:
    value = clean(value)
    if not value or value in {"EDIT_ME", "NOT_APPROVED_UNTIL_FILLED"}:
        return []
    return [item.strip() for item in re.split(r"[,;]", value) if item.strip()]


def checked_labels() -> set[str]:
    checked: set[str] = set()
    text = (ENGAGEMENT / "Engagement-Info.md").read_text(encoding="utf-8")
    for raw in text.splitlines():
        match = re.match(r"^-\s+\[([xX ])\]\s+(.+)$", raw.strip())
        if match and match.group(1).lower() == "x":
            checked.add(match.group(2).strip().lower())
    return checked


def yaml_scalar(value: str) -> str:
    if value == "":
        return "''"
    if re.fullmatch(r"(?:true|false|[0-9]+)", value):
        return value
    return "'" + value.replace("'", "''") + "'"


def write_config(fields: dict[str, str]) -> None:
    checked = checked_labels()
    permission_labels = {
        "allow_external_side_effects": "email/webhook/report delivery tests approved",
        "allow_oob": "ssrf/oob tests approved",
        "allow_state_changes": "disposable object creation and cleanup approved",
        "allow_file_upload": "file-upload tests approved",
        "allow_websocket_frames": "websocket frame/message tests approved",
    }
    hosts = list_value(fields.get("approved_hostnames", ""))
    ips = list_value(fields.get("approved_ips_cidrs", ""))
    ports = list_value(fields.get("approved_ports_protocols", ""))
    ports = [re.sub(r"[^0-9]", "", port) for port in ports if re.search(r"[0-9]", port)] or ["443"]
    tenants = list_value(fields.get("default_tenants", fields.get("default_tenant_s", "")))
    lines = [
        "# GENERATED FILE — edit engagement/*.md, then run scripts/build-machine-state.py.",
        f"project_name: {yaml_scalar(fields.get('project_name', 'EDIT_ME'))}",
        f"client: {yaml_scalar(fields.get('client', 'EDIT_ME'))}",
        f"engagement_id: {yaml_scalar(fields.get('engagement_id', 'EDIT_ME'))}",
        f"assessment_type: {yaml_scalar(fields.get('assessment_type', 'web_application'))}",
        f"owner_pentest_firm: {yaml_scalar(fields.get('owner_pentest_firm', 'EDIT_ME'))}",
        f"primary_tester: {yaml_scalar(fields.get('primary_tester', 'EDIT_ME'))}",
        f"authorization_reference: {yaml_scalar(fields.get('authorization_reference', 'EDIT_ME'))}",
        f"primary_url: {yaml_scalar(fields.get('primary_url', 'https://EDIT_ME/'))}",
        "hosts:",
        *[f"  - {yaml_scalar(item)}" for item in hosts],
        "ips:",
        *[f"  - {yaml_scalar(item)}" for item in ips],
        "ports:",
        *[f"  - {yaml_scalar(item)}" for item in ports],
        f"start_utc: {yaml_scalar(fields.get('start_utc', 'EDIT_ME'))}",
        f"end_utc: {yaml_scalar(fields.get('end_utc', 'EDIT_ME'))}",
        f"timezone: {yaml_scalar(fields.get('date_time_zone', 'UTC'))}",
        f"burp_mcp_endpoint: {yaml_scalar(fields.get('burp_mcp_endpoint', 'http://127.0.0.1:9876'))}",
        f"browser: {yaml_scalar(fields.get('browser', 'EDIT_ME'))}",
        f"excluded_assets: {yaml_scalar(fields.get('excluded_assets', 'EDIT_ME'))}",
        f"emergency_contact: {yaml_scalar(fields.get('emergency_contact', 'EDIT_ME'))}",
        f"stop_condition_contact: {yaml_scalar(fields.get('stop_condition_contact', 'EDIT_ME'))}",
        f"burp_project_evidence_location: {yaml_scalar(fields.get('burp_project_evidence_location', 'private/'))}",
        f"direct_target_traffic_permitted: {yaml_scalar(fields.get('direct_target_traffic_permitted', 'NO — use Burp MCP unless explicitly changed'))}",
        f"oob_listener: {yaml_scalar(fields.get('oob_listener', 'NOT_APPROVED_UNTIL_FILLED'))}",
        f"fixture_namespace: {yaml_scalar(fields.get('test_data_fixture_namespace', 'EDIT_ME'))}",
        f"allowed_disposable_destination: {yaml_scalar(fields.get('allowed_disposable_destination_s', 'EDIT_ME'))}",
        f"cleanup_procedure: {yaml_scalar(fields.get('required_cleanup_procedure', 'EDIT_ME'))}",
        f"maintenance_windows: {yaml_scalar(fields.get('known_maintenance_windows', 'EDIT_ME'))}",
        f"reporting_requirements: {yaml_scalar(fields.get('reporting_requirements', 'EDIT_ME'))}",
        "default_tenants:",
        *[f"  - {yaml_scalar(item)}" for item in tenants],
        "role_file: config/roles.csv",
        "finding_catalogue: catalogue/Finding-Catalogue.md",
        "endpoint_inventory: plans/Endpoint-Inventory.csv",
        "input_inventory: plans/Input-Point-Inventory.csv",
        "context_bank: resource-bank",
        "context_bank_locator: resource-bank/Resource-Locator.md",
        "llm_playbook_index: llm/playbooks/Playbook-Index.md",
        "evidence_directory: evidence",
        "finding_directory: findings",
    ]
    for key, label in permission_labels.items():
        lines.append(f"{key}: {'true' if label in checked else 'false'}")
    (CONFIG / "engagement.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_roles() -> None:
    rows = all_table_rows(ENGAGEMENT / "Roles-and-Credentials.md")
    field_map = {
        "order": "order",
        "role": "role",
        "username": "username",
        "credential_reference": "credential_ref",
        "tenant": "tenant",
        "enabled": "enabled",
        "notes": "notes",
    }
    headers = ["order", "role", "username", "credential_ref", "tenant", "enabled", "notes"]
    with (CONFIG / "roles.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow({target: row.get(source, "") for source, target in field_map.items()})


def write_inventory(source_name: str, output_name: str, headers: list[str]) -> None:
    rows = all_table_rows(ENGAGEMENT / source_name)
    with (PLANS / output_name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow({header: row.get(header, "") for header in headers})


def main() -> None:
    required = [
        ENGAGEMENT / "Engagement-Info.md",
        ENGAGEMENT / "Roles-and-Credentials.md",
        ENGAGEMENT / "Endpoint-Notes.md",
        ENGAGEMENT / "Input-Point-Notes.md",
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing human-readable source file(s):", *missing, sep="\n- ", file=sys.stderr)
        return 1

    CONFIG.mkdir(exist_ok=True)
    PLANS.mkdir(exist_ok=True)
    write_config(engagement_fields())
    write_roles()
    write_inventory(
        "Endpoint-Notes.md",
        "Endpoint-Inventory.csv",
        [
            "endpoint_id", "method", "host", "path", "discovery_source", "ui_route_workflow",
            "auth_required", "role_reachability", "tenant_scope", "object_scope", "state_change",
            "fixture_required", "status", "evidence_reference", "notes",
        ],
    )
    write_inventory(
        "Input-Point-Notes.md",
        "Input-Point-Inventory.csv",
        [
            "input_id", "finding_family", "role", "method", "path", "location_or_field", "source_type",
            "sink_or_behavior", "content_type", "tenant_scope", "fixture_required", "batch", "status",
            "evidence_reference", "notes",
        ],
    )
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build-finding-plan.py")], check=True)
    print("Generated config/*.yaml/csv and plans/*.csv from engagement/*.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

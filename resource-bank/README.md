# Vulnerability Resource Bank

This is a reusable knowledge/resource layer for the web-application mode and future testing modes.

## Purpose

The resource bank may contain:

- Local knowledge files.
- Links to authoritative online references.
- Payload/operator libraries.
- Detection and evaluation rubrics.
- Framework documentation.
- Versioned regression material.
- Tool-specific adapters or seed references.

It is intentionally unpopulated beyond structure. Add resources only after checking licensing, provenance, version, and whether the material is safe and authorized for the engagement.

## Use during an engagement

1. Map the current application surface and identify the applicable finding family.
2. Select only the relevant resource entries and family notes.
3. Record resource IDs, versions, provenance, applicability, and exclusions in the engagement notes or campaign record.
4. Use the selected material to design approved checks; do not send every listed payload or technique automatically.
5. Re-check the selected material when recon changes the applicable surface or technology.

## Organization

Each vulnerability family has a directory:

```text
resource-bank/<family>/
├── README.md
├── Resource-Locator.md       # optional family-specific locator list
├── local/                    # ignored or separately licensed local material
└── notes/                    # human-readable technique notes
```

Use `Resource-Locator.md` and `templates/Resource-Entry.md` for a consistent record. Do not place secrets, target credentials, raw customer data, or uncontrolled harmful payloads in the repository.

The LLM mode has its own playbook integration under `llm/playbooks/`, while generic LLM safety/red-team references may be indexed here later.

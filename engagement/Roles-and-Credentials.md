# Roles and Credential References

> Human-readable source. Edit this file; do not edit `config/roles.csv` directly. Store passwords and tokens only in ignored `private/` storage or a password manager.

The required testing order is highest privilege to lowest privilege:

1. Super Admin
2. Admin
3. Supervisor
4. Agent

| Order | Role | Username | Credential reference | Tenant | Enabled | Notes |
|---:|---|---|---|---|---|---|
| 1 | Super Admin | `EDIT_ME` | `private/credentials.env` or password manager | `EDIT_ME` | true | Highest privilege; test first |
| 2 | Admin | `EDIT_ME` | `private/credentials.env` or password manager | `EDIT_ME` | true | Test after Super Admin |
| 3 | Supervisor | `EDIT_ME` | `private/credentials.env` or password manager | `EDIT_ME` | true | Test after Admin |
| 4 | Agent | `EDIT_ME` | `private/credentials.env` or password manager | `EDIT_ME` | true | Lowest supplied privilege |

## Role-specific notes

- Super Admin tenant access: `EDIT_ME`
- Admin tenant access: `EDIT_ME`
- Supervisor tenant access: `EDIT_ME`
- Agent tenant access: `EDIT_ME`
- Account provisioning or MFA notes: `EDIT_ME`

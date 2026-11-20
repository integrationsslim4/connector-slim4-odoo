# Slim4 Connector: Odoo Apps Store content
Created by: Jorn Kuijpers | Date: 2026-11-20

Branch: `19.0` (a `20.0` branch will follow). Store price: free (no `price` key). License: OPL-1.

## Files
| File | Status |
|---|---|
| `__manifest__.py` | Merge the store fields into your manifest. Keep your own `data` list. |
| `static/description/index.html` | Final store page |
| `static/description/icon.png` | Final |
| `static/description/images/main_screenshot.png` | Final (check Odoo partner logo use is allowed) |
| `static/description/images/flow.png` | Final |
| `static/description/images/inbound_messages.png` | Final |
| `static/description/images/field_mapping.png` | Final |
| `static/description/images/additional_fields.png` | Final |

## Open for Bas
1. `depends` is set to `'Slim4 - Supply Chain Management'`, taken from the store URL. Check it matches the folder name exactly (spaces and capitals included). Add the Odoo modules the connector reads from directly.
2. All images are final.
3. The icon has to be a real PNG (not a renamed file), otherwise the store shows a white cube.

# Created by: Jorn Kuijpers | Date: 2026-11-20
# --Step 1: Store and module metadata for the Odoo Apps Store (branch 19.0)
{
    'name': 'Slim4 Connector',
    'summary': 'Connect Odoo to Slimstock Slim4 for demand forecasting and inventory optimisation',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Inventory',
    'author': 'Slimstock',
    'website': 'https://www.slimstock.com',
    'support': 'integrations@slimstock.com',
    'license': 'OPL-1',
    # --Step 2: Dependencies
    # Technical name taken from the store URL (folder name of the module, spaces included).
    # Bas: add any Odoo modules the connector reads from directly (e.g. 'stock', 'purchase', 'sale').
    'depends': ['base', 'Slim4 - Supply Chain Management'],
    # --Step 3: Data files (Bas: keep your existing list)
    'data': [],
    # --Step 4: Store images (first file ending in _screenshot is the cover)
    'images': ['static/description/images/main_screenshot.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    # No 'price' key: the app is free on the store. Use requires a Slim4 contract.
}

{
    'name' : 'OTA Add Dimension Lot',
    'summary' : 'Custom Module Request 1',
    'version': '1.0',
    'category': 'SMAM/SMAM',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'depends': ['base','mrp','stock'],
    'description': """
Custom Module Request 1
===============================================

1. Add Compute Done = Panjang x Lebar x Tebal in Inventory/Manufacturing Operation Type/By-Products/Detailed Operations
2. Add On Hand Lot on Inventory - Detailed Operations
    """,
    'data': [
        'views/stock_move.xml',
        'views/stock_quant.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
{
    'name' : 'Midtrans',
    'summary' : 'Midtrans Integration',
    'version': '0.1',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'API/Integration',
    'depends': ['base'],
    'description': """
Modul Midtrans.
===============================================

Modul Midtrans that integrate odoo with midtrans
    """,
    'data': [
        'views/unitek_midtrans_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
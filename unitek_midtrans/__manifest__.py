{
    'name' : 'Midtrans',
    'summary' : 'Midtrans Integration',
    'version': '0.2',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'API/Integration',
    'depends': ['base','account','unitek_api_history'],
    'description': """
Modul Midtrans.
===============================================

Modul Midtrans that integrate odoo with midtrans
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/unitek_midtrans_views.xml',
        'views/unitek_midtrans_company_views.xml',
        'views/unitek_midtrans_accountmove_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
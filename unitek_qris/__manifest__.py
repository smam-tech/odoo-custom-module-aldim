{
    'name' : 'QRIS',
    'summary' : 'QRIS Integration',
    'version': '1.0',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'API/Integration',
    'depends': ['base','account','unitek_api_history'],
    'description': """
Modul QRIS payment.
===============================================

Modul QRIS that extends payment in odoo so can print qris.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/unitek_account_move_view.xml',
        'views/unitek_company_ext_api_view.xml',
        'views/unitek_qris_view.xml',
        'report/unitek_account_move_report.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
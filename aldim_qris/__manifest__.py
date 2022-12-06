{
    'name' : 'QRIS payment',
    'version': '1.0',
    'category': 'API/QRIS',
    'depends': ['base','sale'],
    'description': """
Modul QRIS payment.
===============================================

Modul QRIS that extends payment in odoo so can print qris.
    """,
    'data': [
        'views/aldim_qris_view.xml',
        'views/aldim_company_ext_api_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
{
    'name' : 'Jubelio Omnichannel',
    'version': '1.0',
    'category': 'API/QRIS',
    'depends': ['base','product','aldim_api_history'],
    'description': """
Modul Jubelio Omnichannel.
===============================================

Modul Jubelio Omnichannel that integrate odoo data with Jubelio data.
    """,
    'data': [
        'views/aldim_qris_view.xml',
        'views/aldim_company_ext_api_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
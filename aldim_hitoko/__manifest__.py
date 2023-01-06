{
    'name' : 'Hitoko Omnichannel',
    'version': '0.2',
    'category': 'API/QRIS',
    'depends': ['base','product','aldim_api_history'],
    'description': """
Modul Hitoko Omnichannel.
===============================================

Modul Hitoko Omnichannel that integrate odoo data with Jubelio data.
    """,
    'data': [
        'views/aldim_hitoko_company_ext_api.xml',
        'views/aldim_hitoko_product_category.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
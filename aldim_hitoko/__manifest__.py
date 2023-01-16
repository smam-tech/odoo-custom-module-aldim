{
    'name' : 'Hitoko',
    'summary' : 'Hitoko Omnichannel Integration',
    'version': '0.1',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'API/Integration',
    'depends': ['base','product','aldim_api_history','aldim_imgbb'],
    'description': """
Modul Hitoko Omnichannel.
===============================================

Modul Hitoko Omnichannel that integrate odoo data with Jubelio data.
    """,
    'data': [
        'views/aldim_hitoko_res_config_settings.xml',
        'views/aldim_hitoko_product_template.xml',
        'views/aldim_hitoko_product_category.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
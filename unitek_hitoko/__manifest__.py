{
    'name' : 'Hitoko',
    'summary' : 'Hitoko Omnichannel Integration',
    'version': '0.11',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'API/Integration',
    'depends': ['base','product','stock','unitek_api_history','unitek_imgbb'],
    'description': """
Modul Hitoko Omnichannel.
===============================================

Modul Hitoko Omnichannel that integrate odoo data with Jubelio data.
    """,
    'data': [
        'views/unitek_hitoko_res_config_settings.xml',
        'views/unitek_hitoko_stock_warehouse.xml',
        'views/unitek_hitoko_product_template.xml',
        'views/unitek_hitoko_product_category.xml',
        'views/unitek_hitoko_product_product.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
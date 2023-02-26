{
    'name' : 'Unitek POS Pack',
    'summary' : 'Unitek PosPack',
    'version': '1.0',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'Sales/Point of Sale',
    'depends': ['base','sale','stock','contacts','account','purchase','point_of_sale'],
    'description': """
POSPACK
    """,
    'data': [
        'security/access_group.xml',
        'views/unitek_invisible_menu.xml',
        # 'views/unitek_pospack_pos_hide_allcontrol_productmenu.xml',
        # 'views/unitek_pospack_pos_hide_customerbutton_product.xml',
        # 'views/unitek_pospack_pos_hide_inoutbutton.xml',
        # 'views/unitek_pospack_pos_hide_orderbutton.xml',
        'views/unitek_pospack_inventory.xml',
        'views/unitek_pospack_product_template.xml',
        'views/unitek_pospack_purchase.xml',
        'views/unitek_pospack_res_partner.xml',
        'views/unitek_pospack_sale.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
{
    'name' : 'Unitek Custom Module',
    'summary' : 'Unitek Custom Module',
    'version': '1.2',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'Unitek/Training',
    'summary': 'Modul Custom Unitek',
    'depends': ['base','sale'],
    'description': """
Modul Custom Unitek.
===============================================

Modul Custom.
    """,
    'data': [
        'security/ir.model.access.csv',
        'data/unitek.first.csv',
        'views/unitek_first_views.xml',
        # 'views/unitek_first_menu.xml'
        # 'views/unitek_ext_sales_view.xml',
        # 'report/unitek_ext_sales_report.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
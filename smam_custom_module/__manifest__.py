{
    'name' : 'SMAM Custom Module',
    'summary' : 'Custom Module',
    'version': '1.0',
    'category': 'API/Dependency',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'depends': ['base','sale'],
    'description': """
SMAM Custom Module.
===============================================

SMAM Custom Module
    """,
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
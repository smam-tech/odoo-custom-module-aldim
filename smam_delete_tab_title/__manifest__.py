{
    'name' : 'Delete Tab Title',
    'summary' : 'Delete Tab Title',
    'version': '1.0',
    'category': 'Etc/Etc',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'depends': ['base','web'],
    'description': """
Delete Tab Title.
===============================================

Delete Tab Title (Normally Odoo)
    """,
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        'data/demo_data.xml',
        'views/favicon.xml',
    ],
    'assets': {
        'web.assets_backend_prod_only': [
            'odoo-custom-module-aldim/static/src/js/favicon.js',
        ],
    },
}
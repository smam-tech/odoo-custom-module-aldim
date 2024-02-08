{
    'name' : 'SMAM Material',
    'summary' : 'This module created to finish selection process at Keda',
    'version': '1.0',
    'category': 'SMAM/SMAM',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'depends': ['base'],
    'description': """
Modul SMAM Material.
===============================================

This module created to finish selection process at Keda
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/smam_material_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
{
    'name' : 'API History',
    'summary' : 'AldiM API History Receiver',
    'version': '1.0',
    'category': 'API/Dependency',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'summary': 'Modul to document every API History',
    'depends': ['base','sale'],
    'description': """
Modul Custom AldiM.
===============================================

Modul to document every API History, so tracking problem will be easier
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/aldim_api_history_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
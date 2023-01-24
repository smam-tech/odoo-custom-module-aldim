{
    'name' : 'ImgBB',
    'summary' : 'ImgBB Integration',
    'version': '1.0',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'API/Dependency',
    'depends': ['base','unitek_api_history'],
    'description': """
Modul Upload Image.
===============================================

Modul to send image to the imgbb and get imgbb link of the uploaded image.
    """,
    'data': [
        'views/unitek_imgbb_res_config_settings.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
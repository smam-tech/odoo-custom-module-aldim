{
    'name' : 'Sales Extended AldiM',
    'summary' : 'Sales Extended AldiM',
    'version': '1.2',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'AldiM/Training',
    'depends': ['base','sale'],
    'description': """
Modul Sales AldiM.
===============================================

Modul sales dengan adanya tambahan end_user sebagai tujuan akhir
penerima barang.
    """,
    'data': [
        'views/aldim_ext_sales_view.xml',
        'report/aldim_ext_sales_report.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
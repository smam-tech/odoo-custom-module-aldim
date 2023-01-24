{
    'name' : 'Sales Extended Unitek',
    'summary' : 'Sales Extended Unitek',
    'version': '1.2',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'category': 'Unitek/Training',
    'depends': ['base','sale'],
    'description': """
Modul Sales Unitek.
===============================================

Modul sales dengan adanya tambahan end_user sebagai tujuan akhir
penerima barang.
    """,
    'data': [
        'views/unitek_ext_sales_view.xml',
        'report/unitek_ext_sales_report.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
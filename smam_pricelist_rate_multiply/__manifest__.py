{
    'name' : 'Pricelist Rate Multiply',
    'summary' : 'Multiply Price based on Rate',
    'version': '1.0',
    'category': 'Sales/Sales',
    'author': 'Aldi Mulyawan [aldismartkid@gmail.com]',
    'depends': ['base','product'],
    'description': """
Pricelist Rate Multiply.
===============================================

Default price is 1
rate calculation is by multiplying the price with the rate,
for example if you put the rate as 2.5 then the price will
be 2.5 times than normal or increased by 150%
    """,
    'data': [
        'views/pricelist.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
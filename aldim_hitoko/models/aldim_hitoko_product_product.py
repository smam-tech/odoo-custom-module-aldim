from odoo import fields,models,api
import requests
from odoo.exceptions import UserError
#raise UserError('bruh')
import base64
from urllib.request import urlopen

class aldim_hitoko_product_product_model(models.Model):
    _inherit='product.product'
    _description='Integration with Hitoko'

    sku_code_hitoko = fields.Char(
        string='SKU Code Hitoko',
        help='SKU Code that registered with hitoko. MUST BE UNIQUE',
        default=''
    )

    stock_hitoko = fields.Float(
        string='Stock Hitoko',
        help='Stock QTY that will be sent to hitoko, the ammount is added for each warehouse that have sync_hitoko as true',
        readonly=True, 
        digits='Product Unit of Measure'
    )

    def hitoko_test_value(self):
        text = ""
        stocks = self.stock_quant_ids
        for stock in stocks:
            text = text + "product name = " + str(stock.name) + "Product warehouse = " + str(stock.warehouse_id)
        raise UserError(text)
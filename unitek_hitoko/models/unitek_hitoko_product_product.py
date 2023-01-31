from odoo import fields,models,api
import requests
from odoo.exceptions import UserError
#raise UserError('bruh')
import base64
from urllib.request import urlopen

class unitek_hitoko_product_product_model(models.Model):
    _inherit='product.product'
    _description='Integration with Hitoko'

    sku_code_hitoko = fields.Integer(
        string='SKU Code Hitoko',
        help='SKU Code that registered with hitoko. MUST BE UNIQUE',
    )

    stock_hitoko = fields.Float(
        string='Stock Hitoko',
        help='Stock QTY that will be sent to hitoko, the ammount is added for each warehouse that have sync_hitoko as true',
        readonly=True, 
        digits='Product Unit of Measure',
        compute= '_compute_stock_hitoko',        
    )

    def update_variant_price_hitoko(self):
        url = "https://www.hitoko.co.id/erp/api/v1/product/update-price"
        for product in self:
            passparams = {
                'sku_id' : product.sku_code_hitoko,
                'sku_price' : int(round(product.lst_price))
            }
            sign = self.env['unitek.hitoko'].generate_signature_hitoko(product,passparams)
            sentparams = {
                'client_id':self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_id_hitoko'),
                'sign': sign,
                'access_token':self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.access_token_hitoko')
            }
            response = requests.post(url, data=sentparams)
            res = response.json()
            vals = {
                'api_provider' : 'Hitoko',
                'api_prodivder_link' : url,
                'api_method' : 'post',
                'params' : str(passparams),
                'response' : str(res),
                'description' : 'Update Product price for hitoko sku code ' + str(product.sku_code_hitoko) + ' into ' + str(product.lst_price)
            }
            self.env['unitek.api.history'].create(vals)

    def send_variant_stock_hitoko(self):
        url = "https://www.hitoko.co.id/erp/api/v1/product/update-stock"
        for product in self :
            passparams = {
                'sku_id' : product.sku_code_hitoko,
                'stock' : int(product.stock_hitoko)
            }
            sign = self.env['unitek.hitoko'].generate_signature_hitoko(product,passparams)
            sentparams = {
                'client_id':self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_id_hitoko'),
                'sign': sign,
                'access_token':self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.access_token_hitoko')
            }
            response = requests.post(url, data=sentparams)
            res = response.json()
            vals = {
                'api_provider' : 'Hitoko',
                'api_prodivder_link' : url,
                'api_method' : 'post',
                'params' : str(passparams),
                'response' : str(res),
                'description' : 'Update Product Stock'
            }
            self.env['unitek.api.history'].create(vals)


    @api.depends('qty_available')
    def _compute_stock_hitoko(self):
        sync_warehouse = self.env['stock.warehouse'].search([['sync_hitoko', '=', True]])
        for product in self:
            qty_total = 0.0
            for warehouse in sync_warehouse:
                qty = product.with_context(warehouse=warehouse.id).qty_available
                qty_total = qty_total+qty
            product.stock_hitoko = qty_total

    def hitoko_test_value(self):
        raise UserError("ok")
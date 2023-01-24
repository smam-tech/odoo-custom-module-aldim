from odoo import fields,models,api
import requests
from odoo.exceptions import UserError
#raise UserError('bruh')
import base64
from urllib.request import urlopen

class unitek_hitoko_stock_warehouse_model(models.Model):
    _inherit='stock.warehouse'
    _description='Integration with Hitoko'

    sync_hitoko = fields.Boolean(
        string='Sync Hitoko',
        help='Check if you want to sync stock in this warehouse to be sent to hitoko',
    )
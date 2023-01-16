from odoo import fields,models
from datetime import datetime
import time

class aldim_api_history(models.Model):
    _name = "aldim.api.history"
    _description = "API History Model"

    api_provider = fields.Char(
        string='API Provider',
        readonly='True',
        help='Provider API yang mengirimkan Response'
    )

    api_prodivder_link = fields.Char(
        string='Link',
        readonly='True',
        help='Link Provider API yang mengirimkan Response'
    )

    date_api = fields.Datetime(
        string='Tanggal',
        readonly='True',
        help='Tanggal Penerimaan Response',
        default= fields.Datetime.now
    )

    api_method = fields.Char(
        string='Method',
        readonly='True',
        help='Method to call the API'
    )

    description = fields.Char(
        string='Description',
        readonly='True',
        help='What the api call function',
        default='DESCRIPTION EMPTY, PLS CONTACT aldismartkid@gmail.com and tell what happen.'
    )

    params = fields.Text(
        string='Parameter',
        readonly='True',
        help='API Response in JSON Format'
    )

    response = fields.Text(
        string='Response',
        readonly='True',
        help='API Response Received'
    )
from odoo import fields,models

class aldim_api_history_model(models.Model):
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

    date = fields.datetime(
        string='Tanggal',
        readonly='True',
        help='Tanggal Penerimaan Response'
    )

    params = fields.Text(
        string='Response',
        readonly='True',
        help='API Response in JSON Format'
    )

    response = fields.Text(
        string='Response',
        readonly='True',
        help='API Response Received'
    )
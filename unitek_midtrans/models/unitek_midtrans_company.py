from odoo import fields,models,api
from . import midtransclient as midtrans
import base64

class unitek_midtrans_company_model(models.Model):
    _inherit='res.company'
    _description='Company extend for API key and Midtrans mID'

    midtrans_server_key = fields.Char(
        string='Midtrans SERVER_KEY',
        help='get your server key at https://dashboard.sandbox.midtrans.com/settings/config_info'
    )

    midtrans_auth_string = fields.Char(
        string='Midtrans auth string',
        help='generated auth string by doing "midtrans_server_key:" and make it base64',
        compute="_compute_midtrans_auth_string",
        store=True
    )

    @api.depends('midtrans_server_key')
    def _compute_midtrans_auth_string(self):
        for key in self:
            if key.midtrans_server_key:
                key.midtrans_auth_string = base64.b64encode(key.midtrans_server_key+":")

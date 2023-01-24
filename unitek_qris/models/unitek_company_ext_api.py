from odoo import fields,models

class unitek_company_ext_api_model(models.Model):
    _inherit='res.company'
    _description='Company extend for API key and QRIS mID'

    qris_api_key = fields.Char(
        string='API Key QRIS',
        help='API Key untuk QRIS, Cek web QRIS untuk info lebih lanjut'
    )
    qris_mid = fields.Char(
        string='mID untuk QRIS',
        help='mID untuk QRIS, Cek web QRIS untuk info lebih lanjut'
    )
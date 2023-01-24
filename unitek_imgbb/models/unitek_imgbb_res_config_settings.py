from odoo import fields,models
import json
import requests

class unitek_imgbb_res_config_settings_model(models.TransientModel):
    _inherit='res.config.settings'
    _description='Config extend for API token with Hitoko'

    key_imgbb = fields.Char(
        string='API Key imgbb',
        help='API Key for imgbb, get your API key at https://api.imgbb.com/',
        default='',
        config_parameter='unitek_imgbb.key_imgbb'
    )

    time_imgbb = fields.Integer(
        string='Time Valid imgbb',
        help='Time Image stay at imgbb, in second',
        default=60000,
        config_parameter='unitek_imgbb.time_imgbb'
    )
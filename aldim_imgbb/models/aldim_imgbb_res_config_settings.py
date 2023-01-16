from odoo import fields,models
import json
import requests

class aldim_imgbb_res_config_settings_model(models.TransientModel):
    _inherit='res.config.settings'
    _description='Config extend for API token with Hitoko'

    key_imgbb = fields.Char(
        string='API Key imgbb',
        help='API Key for imgbb, get your API key at https://api.imgbb.com/',
        default='',
        config_parameter='aldim_imgbb.key_imgbb'
    )

    time_imgbb = fields.Integer(
        string='Time Valid imgbb',
        help='Time Image stay at imgbb, in second',
        default=60000,
        config_parameter='aldim_imgbb.time_imgbb'
    )

    def convert_image_to_link(self,passself,imagebase64,time=60000):
        url = 'https://api.imgbb.com/1/upload'
        reqparams = {
            'key':passself.env['ir.config_parameter'].sudo().get_param('aldim_imgbb.key_imgbb'),
            'image': imagebase64,
            'expiration':str(passself.env['ir.config_parameter'].sudo().get_param('aldim_imgbb.time_imgbb'))
        }
        response = requests.post(url, data=reqparams)
        res = response.json()
        vals = {
            'api_provider' : 'ImgBB',
            'api_prodivder_link' : url,
            'api_method' : 'post',
            'params' : str(reqparams),
            'response' : str(res),
            'description' : 'Uploading image and getting public image url for model ' + str(passself)
        }
        self.env['aldim.api.history'].create(vals)
        if 'data' in res.keys():
            return res['data']['url']
        else:
            return 'ERROR CHECK API HISTORY'
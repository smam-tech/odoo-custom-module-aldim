from odoo import fields,models
import json
import requests

class UnitekImgbb(models.Model):
    _name = "unitek.imgbb"
    _description = "ImgBB Integration"

    def convert_image_to_link(self,passself,imagebase64,time=60000):
        url = 'https://api.imgbb.com/1/upload'
        reqparams = {
            'key':passself.env['ir.config_parameter'].sudo().get_param('unitek_imgbb.key_imgbb'),
            'image': imagebase64,
            'expiration':str(passself.env['ir.config_parameter'].sudo().get_param('unitek_imgbb.time_imgbb'))
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
        self.env['unitek.api.history'].create(vals)
        if 'data' in res.keys():
            return res['data']['url']
        else:
            return 'ERROR CHECK API HISTORY'
    

from odoo import fields,models
import json
import requests

class aldim_hitoko_res_config_settings_model(models.TransientModel):
    _inherit='res.config.settings'
    _description='Config extend for API token with Hitoko'

    client_id_hitoko = fields.Char(
        string='Client ID HiToko',
        help='Client ID yang terdaftar API Hitoko, Cek web Hitoko untuk info lebih lanjut',
        default='',
        config_parameter='aldim_hitoko.client_id_hitoko'
    )

    client_secret_hitoko = fields.Char(
        string='Client Secret Hitoko',
        help='Client Secret yang terdaftar API Hitoko, Cek web Hitoko untuk info lebih lanjut',
        default='',
        config_parameter='aldim_hitoko.client_secret_hitoko'
    )

    access_token_hitoko = fields.Char(
        string='Accest Token Hitoko',
        readonly='True',
        help='Token yang didapat setiap ada request, Masa aktif 12 jam',
        default='',
        config_parameter='aldim_hitoko.access_token_hitoko'
    )

    type_token_hitoko = fields.Char(
        string='Token Type Hitoko',
        readonly='True',
        help='Token Tipe Hitoko',
        default='',
        config_parameter='aldim_hitoko.type_token_hitoko'
    )

    refresh_token_hitoko = fields.Char(
        string='Refresh Token Hitoko',
        readonly='True',
        help='Refresh Token, Expire in 30d, For getting new access token',
        default='',
        config_parameter='aldim_hitoko.refresh_token_hitoko'
    )
    expire_token_hitoko = fields.Integer(
        string='Time Token Expire Hitoko',
        readonly='True',
        help='Expire time for last requested token in hitoko',
        default='',
        config_parameter='aldim_hitoko.expire_token_hitoko'
    )   

    def hitoko_post_retrieve_token(self,passparams):
        url = 'https://www.hitoko.co.id/erp/oauth/token'
        response = requests.post(url, params=passparams)
        res = response.json()
        vals = {
            'api_provider' : 'Hitoko',
            'api_prodivder_link' : url,
            'api_method' : 'post',
            'params' : str(passparams),
            'response' : str(res),
            'description' : 'Retrieve Hitoko Token for auth'
        }
        self.env['aldim.api.history'].create(vals)
        return res


    def hitoko_retrieve_token(self):
        passparamsvar = {
            'client_id' : self.client_id_hitoko,
            'client_secret' : self.client_secret_hitoko,
            'grant_type' : 'client_credentials'
        }
        res = aldim_hitoko_res_config_settings_model.hitoko_post_retrieve_token(self,passparamsvar)
        if 'access_token' in res.keys() :
            self.expire_token_hitoko = res['expires_in']
            self.type_token_hitoko = res['token_type']
            self.access_token_hitoko = res['access_token']
            self.refresh_token_hitoko = res['refresh_token']
        else :
            self.expire_token_hitoko = fields.Datetime.now
            self.type_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
            self.access_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
            self.refresh_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'

    
    def hitoko_refresh_token(self):
        passparamsvar = {
            'grant_type' : 'refresh_token',
            'client_id' : self.client_id_hitoko,
            'client_secret' : self.client_secret_hitoko,
            'refresh_token' : self.refresh_token_hitoko
        }
        res = aldim_hitoko_res_config_settings_model.hitoko_post_retrieve_token(self,passparamsvar)
        if 'access_token' in res.keys() :
            self.expire_token_hitoko = res['expires_in']
            self.type_token_hitoko = res['token_type']
            self.access_token_hitoko = res['access_token']
            self.refresh_token_hitoko = res['refresh_token']
        else :
            self.expire_token_hitoko = fields.Datetime.now
            self.type_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
            self.access_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
            self.refresh_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
        
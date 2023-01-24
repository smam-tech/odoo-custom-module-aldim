from odoo import fields,models
import json
import requests

class unitek_hitoko_res_config_settings_model(models.TransientModel):
    _inherit='res.config.settings'
    _description='Config extend for API token with Hitoko'

    client_id_hitoko = fields.Char(
        string='Client ID HiToko',
        help='Client ID yang terdaftar API Hitoko, Cek web Hitoko untuk info lebih lanjut',
        default='',
        config_parameter='unitek_hitoko.client_id_hitoko'
    )

    client_secret_hitoko = fields.Char(
        string='Client Secret Hitoko',
        help='Client Secret yang terdaftar API Hitoko, Cek web Hitoko untuk info lebih lanjut',
        default='',
        config_parameter='unitek_hitoko.client_secret_hitoko'
    )

    access_token_hitoko = fields.Char(
        string='Accest Token Hitoko',
        readonly='True',
        help='Token yang didapat setiap ada request, Masa aktif 12 jam',
        default='',
        config_parameter='unitek_hitoko.access_token_hitoko'
    )

    type_token_hitoko = fields.Char(
        string='Token Type Hitoko',
        readonly='True',
        help='Token Tipe Hitoko',
        default='',
        config_parameter='unitek_hitoko.type_token_hitoko'
    )

    refresh_token_hitoko = fields.Char(
        string='Refresh Token Hitoko',
        readonly='True',
        help='Refresh Token, Expire in 30d, For getting new access token',
        default='',
        config_parameter='unitek_hitoko.refresh_token_hitoko'
    )
    expire_token_hitoko = fields.Integer(
        string='Time Token Expire Hitoko',
        readonly='True',
        help='Expire time for last requested token in hitoko',
        default=0,
        config_parameter='unitek_hitoko.expire_token_hitoko'
    )

    def hitoko_post_retrieve_token(self,passparams):
        url = 'https://www.hitoko.co.id/erp/oauth/token'
        response = requests.post(url, data=passparams)
        res = response.json()
        vals = {
            'api_provider' : 'Hitoko',
            'api_prodivder_link' : url,
            'api_method' : 'post',
            'params' : str(passparams),
            'response' : str(res),
            'description' : 'Retrieve Hitoko Token for auth'
        }
        self.env['unitek.api.history'].create(vals)
        return res


    def hitoko_retrieve_token(self):
        passparamsvar = {
            'client_id' : self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_id_hitoko'),
            'client_secret' : self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_secret_hitoko'),
            'grant_type' : 'client_credentials'
        }
        res = unitek_hitoko_res_config_settings_model.hitoko_post_retrieve_token(self,passparamsvar)
        if 'access_token' in res.keys() :
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.expire_token_hitoko',res['expires_in'])
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.type_token_hitoko',res['token_type'])
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.access_token_hitoko',res['access_token'])
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.refresh_token_hitoko',res['refresh_token']) 
            # self.expire_token_hitoko = res['expires_in']
            # self.type_token_hitoko = res['token_type']
            # self.access_token_hitoko = res['access_token']
            # self.refresh_token_hitoko = res['refresh_token']
        else :
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.expire_token_hitoko',0)
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.type_token_hitoko','Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token')
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.access_token_hitoko','Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token')
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.refresh_token_hitoko','Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token')
            # self.expire_token_hitoko = 0
            # self.type_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
            # self.access_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
            # self.refresh_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'

    
    def hitoko_refresh_token(self):
        passparamsvar = {
            'grant_type' : 'refresh_token',
            'client_id' : self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_id_hitoko'),
            'client_secret' : self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_secret_hitoko'),
            'refresh_token' : self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.refresh_token_hitoko')
        }
        res = unitek_hitoko_res_config_settings_model.hitoko_post_retrieve_token(self,passparamsvar)
        if 'access_token' in res.keys() :
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.expire_token_hitoko',res['expires_in'])
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.type_token_hitoko',res['token_type'])
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.access_token_hitoko',res['access_token'])
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.refresh_token_hitoko',res['refresh_token'])            
            # self.expire_token_hitoko = res['expires_in']
            # self.type_token_hitoko = res['token_type']
            # self.access_token_hitoko = res['access_token']
            # self.refresh_token_hitoko = res['refresh_token']
        else :
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.expire_token_hitoko',0)
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.type_token_hitoko','Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token')
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.access_token_hitoko','Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token')
            self.env['ir.config_parameter'].sudo().set_param('unitek_hitoko.refresh_token_hitoko','Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token')            
            # self.expire_token_hitoko = 0
            # self.type_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
            # self.access_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
            # self.refresh_token_hitoko = 'Please check API History with filter method = post, and link https://www.hitoko.co.id/erp/oauth/token'
        
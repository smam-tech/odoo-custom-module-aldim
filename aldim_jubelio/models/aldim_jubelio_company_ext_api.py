from odoo import fields,models
import json
import requests

class aldim_jubelio_company_ext_api_model(models.Model):
    _inherit='res.company'
    _description='Company extend for Api Token Jubelio'

    email_jubelio = fields.Char(
        string='Email Jubelio',
        help='Email yang terdaftar API Jubelio, Cek web Jubelio untuk info lebih lanjut'
    )

    password_jubelio = fields.Char(
        string='Password Jubelio',
        help='Password untuk email yang terdaftar API Jubelio, Cek web Jubelio untuk info lebih lanjut'
    )

    token_jubelio = fields.Char(
        string='Token Jubelio',
        readonly='True',
        help='Token yang didapat setiap ada request, Masa aktif 12 jam'
    )

    time_token_jubelio = fields.Datetime(
        string='Last Token Time Jubelio',
        readonly='True',
        default= fields.Datetime.now,
        help='Waktu terakhir kali dilakukan request token untuk jubelio'
    )

    def jubelio_api_post_token_account(self,passparams):
        url = "https://api.jubelio.com/login"
        response = requests.post(url, params=passparams)
        res = response.json()
        vals = {
            'api_provider' : 'Jubelio',
            'api_prodivder_link' : url,
            'api method' : 'post',
            'params' : str(passparams),
            'response' : str(res)    
        }
        self.env['aldim.api.history'].create(vals)
        return res

    def jubelio_token_account(self):
        passparamsvar = {
            'email' : self.email_jubelio,
            'password' : self.password_jubelio
        }
        res = aldim_jubelio_company_ext_api_model.jubelio_api_post_token_account(self,passparamsvar)
        if 'statusCode' in res.keys() :
            if res['statusCode']!= 200 :
                self.time_token_jubelio = fields.Datetime.now
                self.token_jubelio = 'Please check API History with filter time as above, method = post, and link https://api.jubelio.com/login'
                return
        self.token_jubelio = res['token']
        self.time_token_jubelio = fields.Datetime.now
        
## This one for Product Category
from odoo import fields,models
import requests


class aldim_hitoko_product_category_model(models.Model):
    _inherit='product.category'
    _description='Integration with Hitoko'

    category_id_hitoko = fields.Integer(
        string='Category ID Hitoko',
        readonly='True',
        help='Product Category Id in Hitoko'
    )

    parent_id_hitoko = fields.Integer(
        string='Parent ID Hitoko',
        readonly='True',
        help='Product Parent Category Id in Hitoko'
    )

    parent2_id_hitoko = fields.Integer(
        string='Parent2 ID Hitoko',
        readonly='True',
        help='Product Parent tier 2 Category Id in Hitoko'
    )

    parent3_id_hitoko = fields.Integer(
        string='Parent3 ID Hitoko',
        readonly='True',
        help='Product Parent tier 3 Category Id in Hitoko'
    )

    parent4_id_hitoko = fields.Integer(
        string='Parent4 ID Hitoko',
        readonly='True',
        help='Product Parent tier 4 Category Id in Hitoko'
    )

    parent5_id_hitoko = fields.Integer(
        string='Parent5 ID Hitoko',
        readonly='True',
        help='Product Parent tier 5 Category Id in Hitoko'
    )

    sync_hitoko = fields.Boolean(
        string='Sync Hitoko',
        default=True,
        help='Sync Category With Hitoko'
    )

    def do_sync_product_category_odoo_hitoko(self,res): #Self is self, res is API response
        if res['message'] == 'request success':
            list_cat_hitoko = res['data']
            pick_category = self.env['product.category'].search([('sync_hitoko','=',True)])
            for cat in pick_category :
                for one_cat_hitoko in list_cat_hitoko:
                    if cat.complete_name in one_cat_hitoko['category_name']:
                        cat.category_id_hitoko = one_cat_hitoko['category_id']
                        cat.parent_id_hitoko = one_cat_hitoko['parent_id']

        aldim_hitoko_product_category_model.do_fill_all_parent_product_category_hitoko(self, pick_category)
        return "Done"


## PROBLEM SEARCH WRITE
    def do_fill_all_parent_product_category_hitoko(self,category):
        for cat in category:
            highest_parent = cat.parent_id_hitoko
            count = 1
            while highest_parent != 0 or count < 5 :
                count = count + 1
                same = self.env['product.category'].search([('sync_hitoko','=',True)], limit=1, order='id desc')
                if same:
                    column_filled = 'parent'+str(count)+'_id_hitoko'
                    highest_parent = same.parent_id_hitoko
                    cat.write({column_filled : highest_parent})
                else:
                    highest_parent = 0




    def hitoko_get_retrieve_product_category(self):
        url = 'https://www.hitoko.co.id/erp/api/v1/product/categorys'
        reqparams = {
            'page':1,
            'size':9999999
        }

        sign = self.env['res.company'].generate_signature_hitoko(self,reqparams)
        passparams = {
            'client_id':self.company_id.client_id_hitoko,
            'sign': sign,
            'access_token':self.company_id.access_token_hitoko
        }

        response = requests.post(url, params=passparams)
        res = response.json()
        vals = {
            'api_provider' : 'Hitoko',
            'api_prodivder_link' : url,
            'api method' : 'get',
            'params' : 'Params Sent: \n'+str(passparams)+'\n Params Source : \n'+str(reqparams),
            'response' : str(res)   
        }

        self.env['aldim.api.history'].create(vals)

        aldim_hitoko_product_category_model.do_sync_product_category_odoo_hitoko(self,res)


        

    
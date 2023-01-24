## This one for Product Category
from odoo import fields,models
import requests


class unitek_hitoko_product_category_model(models.Model):
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
            pick_category = self.search([('sync_hitoko','=',True)])
            cat_odoo_missing = []
            for one_cat_hitoko in list_cat_hitoko:
                cat_odoo_missing.append(one_cat_hitoko)
                for cat in pick_category :
            # for cat in pick_category :
                # for one_cat_hitoko in list_cat_hitoko:
                    if cat.complete_name == one_cat_hitoko['category_name']:
                        cat.category_id_hitoko = one_cat_hitoko['category_id']
                        cat.parent_id_hitoko = one_cat_hitoko['parent_id']
                        cat_odoo_missing.pop()
                        continue
        unitek_hitoko_product_category_model.do_fill_missing_category_odoo_hitoko(self,cat_odoo_missing)
        sync_odoo_category = self.search([('sync_hitoko','=',True)])
        unitek_hitoko_product_category_model.do_fill_all_parent_product_category_hitoko(self, sync_odoo_category)
        return "Done"

        ##PROBLEM CHILD_ID (many2one), PARENT_PATH (Char)
    def do_fill_missing_category_odoo_hitoko(self,missing_category):
        for cat in missing_category:
            vals = {
                'name' : cat['category_name'],
                'category_id_hitoko':cat['category_id'],
                'parent_id_hitoko':cat['parent_id']
            }
            self.create(vals)

        for cat in missing_category:
            selected_cat = self.search([
                ('name','=',cat['category_name']),'&',
                ('category_id_hitoko','=',cat['category_id']),'&',
                ('parent_id_hitoko','=',cat['parent_id'])],
                limit=1
                )
            parent_cat = self.search([
                ('category_id_hitoko','=',cat['parent_id'])],
                limit=1
                )
            child_cat = self.search({
                ('parent_id_hitoko','=',cat['category_id'])}
                )
            vals = {
                'parent_id':parent_cat,
                'child_id':child_cat
            }

            selected_cat.write(vals)
            


## PROBLEM_DONE SEARCH WRITE
    def do_fill_all_parent_product_category_hitoko(self,category):
        for cat in category:
            highest_parent = cat.parent_id_hitoko
            count = 1
            while highest_parent != 0 or count < 5 :
                count = count + 1
                same = self.search([('sync_hitoko','=',True)], limit=1, order='id desc')
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

        sign = self.env['unitek.hitoko'].generate_signature_hitoko(self,reqparams)
        passparams = {
            'client_id':self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_id_hitoko'),
            'sign': sign,
            'access_token':self.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.access_token_hitoko')
        }

        response = requests.post(url, data=passparams)
        res = response.json()
        vals = {
            'api_provider' : 'Hitoko',
            'api_prodivder_link' : url,
            'api_method' : 'get',
            'params' : 'Params Sent: \n'+str(passparams)+'\n Params Source : \n'+str(reqparams),
            'response' : str(res),
            'description' : 'Retrieve Product Category from Hitoko to Odoo'
        }

        self.env['unitek.api.history'].create(vals)

        unitek_hitoko_product_category_model.do_sync_product_category_odoo_hitoko(self,res)


        

    
from odoo import fields,models

class aldim_hitoko_product_template_model(models.Model):
    _inherit='product.template'
    _description='Integration with Hitoko'
    
    variant_info_hitoko = fields.Char(
        string='Variant Info Hitoko',
        readonly='True',
        help='Product Variant Info that will be sent to hitoko',
        default=''
    )

    def hitoko_post_create_product(self):
        url = 'https://www.hitoko.co.id/erp/api/v1/product/create'
        reqparams = {
            'product_name':self.name,
            'variant_info':'',
            'sku_info':'',
            'description':'',
            'text_description':'',
            'product_sys_img_list':'',
            'weight':str(self.weight),
            'length':str(self.weight),
            'width':'',
            'height':'',
            'sku_flag':'',
            'category_first_id':self.categ_id.category_id_hitoko,
            'categorySecond_id':self.categ_id.parent_id_hitoko,
            'category_third_id':self.categ_id.parent2_id_hitoko,
            'category_fourth_id':self.categ_id.parent3_id_hitoko,
            'category_fifth_id':self.categ_id.parent4_id_hitoko,
            'category_sixth_id':self.categ_id.parent5_id_hitoko
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

        if res['message'] == 'request success':
            list_cat_hitoko = res['data']
            pick_category = self.env['product.category'].search([('sync_hitoko','=',True)])
            for cat in pick_category :
                for one_cat_hitoko in list_cat_hitoko:
                    if cat.complete_name in one_cat_hitoko['category_name']:
                        cat.category_id_hitoko = one_cat_hitoko['category_id']
                        cat.parent_id_hitoko = one_cat_hitoko['parent_id']
                        continue
from odoo import fields,models,api
import requests
from odoo.exceptions import UserError
#raise UserError('bruh')
import base64
from urllib.request import urlopen

class aldim_hitoko_product_template_model(models.Model):
    _inherit='product.template'
    _description='Integration with Hitoko'
    variant_info_hitoko = fields.Char(
        string='Variant Info Hitoko',
        readonly='True',
        help='Product Variant Info that will be sent to hitoko',
        default=''
    )

    image_link = fields.Char(
        string="Public Image Link",
        readonly='True',
        help='Image link uploaded to https://api.imgbb.com/',
        # compute= '_compute_image_link',
        default= ''
    )

    weight_hitoko = fields.Integer(
        string='Product Weight',
        help='Product Weight that will sent to hitoko, for product delivery cost.',
        default=0
    )

    length_hitoko = fields.Integer(
        string='Product Length',
        help='Product Length that will sent to hitoko, for product delivery cost.',
        default=0
    )

    width_hitoko = fields.Integer(
        string='Product Width',
        help='Product Width that will sent to hitoko, for product delivery cost.',
        default=0
    )

    height_hitoko = fields.Integer(
        string='Product Height',
        help='Product Height that will sent to hitoko, for product delivery cost.',
        default=0
    )

    # @api.depends('image_1920')
    # def _compute_image_link(self):
    #     for template in self:
    #         aldim_hitoko_product_template_model.hitoko_get_image_link(template)


    def hitoko_get_image_link(self,singlerecord=""):
        if singlerecord != "":
            imglink = self.env['res.config.settings'].convert_image_to_link(self,singlerecord.image_1920)
            singlerecord.image_link = imglink
            return "Done"
        for template in self:
            # Format for ir_attachment
            # url = template.get_base_url() + "/web/image/product.template/%s/image_1920" % template.id
            # imgbase64 = base64.b64encode(urlopen(url).read())
            # attachments = self.env['ir.attachment'].sudo().search(
            #     [('res_model', '=', 'product.template'),
            #     ('res_field', '=', 'image_1920'),
            #     ('res_id', '=', template.id)], limit=1)
            # printend = '---store_fname = ' + str(attachments.store_fname) + '---datas = ' + str(attachments.datas) + "---db_datas = " + str(attachments.db_datas) + "---raw = " + str(attachments.raw) + "---file_size = " + str(attachments.file_size)
            # raise UserError(printend)
            # imglink = self.env['res.config.settings'].convert_image_to_link(self,attachments.datas)
            imglink = self.env['res.config.settings'].convert_image_to_link(self,template.image_1920)
            template.image_link = imglink
            return "done"

    def hitoko_test_value(self):
        variants = self.product_variant_ids
        text = ""
        for variant in variants:
            stocks = variant.stock_quant_ids
            for stock in stocks:
                text = text + "product name = " + str(variant.name) + "Product warehouse = " + str(variant.warehouse_id)
        raise UserError(text)


    def hitoko_post_create_product(self):
        url = 'https://www.hitoko.co.id/erp/api/v1/product/create'
        reqparams = {
            'product_name':self.name,
            'variant_info':self.variant_info_hitoko,
            'sku_info':'',
            'description':str(self.description_sale),
            'text_description':str(self.description_sale),
            'product_sys_img_list':'',
            'weight':str(self.weight_hitoko),
            'length':str(self.length_hitoko),
            'width':str(self.width_hitoko),
            'height':str(self.height_hitoko),
            'sku_flag':str(int(self.is_product_variant)),
            'category_first_id':self.categ_id.category_id_hitoko,
            'categorySecond_id':self.categ_id.parent_id_hitoko,
            'category_third_id':self.categ_id.parent2_id_hitoko,
            'category_fourth_id':self.categ_id.parent3_id_hitoko,
            'category_fifth_id':self.categ_id.parent4_id_hitoko,
            'category_sixth_id':self.categ_id.parent5_id_hitoko
        }

        recordcompany = self.company_id
        sign = self.env['res.company'].generate_signature_hitoko(recordcompany,reqparams)
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
            'api_method' : 'get',
            'params' : 'Params Sent: \n'+str(passparams)+'\n Params Source : \n'+str(reqparams),
            'response' : str(res),
            'description' : 'export product at odoo to hitoko with name ' + self.name 
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
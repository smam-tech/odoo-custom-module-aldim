from odoo import fields,models
import json
import requests
import qrcode
import time
import base64
from odoo.exceptions import UserError
from io import BytesIO
from decimal import Decimal, ROUND_HALF_UP

class unitek_account_move_model(models.Model):
    _inherit='account.move'
    _description="Integration with QRIS"

    qris_id = fields.Many2one(
        'unitek.qris',
        string='QRIS',
        readonly='True',
        help='QRIS record that connected'
    )

    qris_image = fields.Image(
        related="qris_id.qris_image"
    )
    
    qris_image_string = fields.Char(
        related="qris_id.qris_image_string"
    )

    qris_status_paid = fields.Char(
        related="qris_id.qris_status_paid"
    )

    qris_status_paid_by_customer = fields.Char(
        related="qris_id.qris_status_paid_by_customer"
    )

    qris_status_paid_by_platform = fields.Char(
        related="qris_id.qris_status_paid_by_platform"
    )

    qris_invoice_id = fields.Char(
        related="qris_id.qris_invoice_id"
    )

    qris_nmid = fields.Char(
        related="qris_id.qris_nmid"
    )

    qris_invoice_request_date = fields.Char(
        related="qris_id.qris_invoice_request_date"
    )

    def qris_check_invoice(self):
        for invoice in self:
            invoice.env['unitek.qris'].qris_check_invoice(invoice.qris_id)
    
    def qris_create_invoice(self):
        for invoice in self:
            invoice.qris_id = invoice.env['unitek.qris'].qris_create_invoice(invoice.name,invoice.amount_residual)

    # def conv_toint_half_up(ininteger):
    #     ininteger = Decimal(ininteger).to_integral_value(rounding=ROUND_HALF_UP)
    #     return ininteger

    # def qris_api_get_create_invoice(self,passparams):
    #     url = "https://qris.id/restapi/qris/show_qris.php"
    #     response = requests.get(url, params=passparams)
    #     res = response.json()
    #     vals = {
    #         'api_provider' : 'QRIS',
    #         'api_prodivder_link' : url,
    #         'api_method' : 'get',
    #         'params' : str(passparams),
    #         'response' : str(res),
    #         'description' : 'Create QRIS Invoice'
    #     }
    #     self.env['unitek.api.history'].create(vals)
    #     return res

    # def convert_qris_string_to_base64img(qris_string):
    #     qrisimg = qrcode.make(qris_string)
    #     buffered = BytesIO()
    #     qrisimg.save(buffered,'JPEG')
    #     qrisbase64 = base64.b64encode(buffered.getvalue())
    #     # raise UserError(str(type(qrisimg))+" AND "+str(type(qrisbase64)))
    #     return qrisbase64
    #     # TypeError: a bytes-like object is required, not 'PilImage'

    # def tes_convert_img(self):
    #     self.qris_image = unitek_qris_model.convert_qris_string_to_base64img(self.qris_image_string)

    # def qris_create_invoice(self):
    #     passparamsvar = {
    #         'do':'create-invoice',
    #         'apikey': self.env.company.qris_api_key,
    #         'mID':self.env.company.qris_mid,
    #         'cliTrxNumber':self.name,
    #         'cliTrxAmount': unitek_qris_model.conv_toint_half_up(self.amount_residual)
    #     }
    #     res = unitek_qris_model.qris_api_get_create_invoice(self,passparamsvar)
    #     if res['status']=='success':
    #         res = res['data']
    #         self.qris_image_string=res['qris_content']
    #         self.qris_invoice_id=res['qris_invoiceid']
    #         self.qris_invoice_request_date=res['qris_request_date']
    #         self.qris_nmid=res['qris_nmid']
    #         self.qris_image = unitek_qris_model.convert_qris_string_to_base64img(self.qris_image_string)
    #     elif res['status']=='failed':
    #         self.qris_invoice_id=str(res['data'])

    # def qris_api_get_check_invoice(self,passparams):
    #     url = "https://qris.id/restapi/qris/checkpaid_qris.php"
    #     response = requests.get(url, params=passparams)
    #     res = response.json()
    #     vals = {
    #         'api_provider' : 'QRIS',
    #         'api_prodivder_link' : url,
    #         'api_method' : 'get',
    #         'params' : str(passparams),
    #         'response' : str(res),
    #         'description' : 'Check QRIS Invoice have been paid or not'
    #     }
    #     self.env['unitek.api.history'].create(vals)
    #     return res

    # # @api.depends('env.company')
    # def qris_check_invoice(self):
    #     passparamsvar = {
    #         'do':'checkStatus',
    #         'apikey': self.env.company.qris_api_key,
    #         'mID':self.env.company.qris_mid,
    #         'invid':self.qris_invoice_id,
    #         'trxvalue':int(round(self.amount_residual)),
    #         'trxdate':self.qris_invoice_request_date[:10]
    #     }
    #     res = unitek_qris_model.qris_api_get_check_invoice(self,passparamsvar)
    #     if res['status']=='success':
    #         res = res['data']
    #         self.qris_status_paid=res['qris_status']
    #         self.qris_status_paid_by_customer=res['qris_payment_customername']
    #         self.qris_status_paid_by_platform=['qris_payment_methodby']
    #     if res['status']=='failed':
    #         res = res['data']
    #         self.qris_status_paid=res['qris_status']

from odoo import fields,models
import json
import requests
import qrcode
import time
import base64
from odoo.exceptions import UserError
from io import BytesIO

class unitek_qris_model(models.Model):
    _inherit='account.move'
    _description="Integration with QRIS"

    qris_image = fields.Image(
        string='Gambar',
        readonly='True',
        help='Generated Image'
    )
    
    qris_image_string = fields.Char(
        string='Gambar-Mentah',
        # readonly='True',
        help='Generated String untuk gambar yang akan di generate, berasal dari API'
    )

    qris_status_paid = fields.Char(
        string='Status Pembayaran',
        readonly='True',
        help='Status apakah sudah dibayar atau belum'
    )

    qris_status_paid_by_customer = fields.Char(
        string='Dibayar Oleh',
        readonly='True',
        default='UNPAID',
        help='Receipt dibayar oleh siapa'
    )

    qris_status_paid_by_platform = fields.Char(
        string='Dibayar Melalui',
        readonly='True',
        default='UNPAID',
        help='Receipt dibayar melalui platform'
    )

    qris_invoice_id = fields.Char(
        string='ID Invoice QRIS',
        readonly='True',
        help='Nomor Transaksi QRIS yang berupa integer yang dapat digunakan untuk memeriksa status pembayaran QRIS'
    )

    qris_nmid = fields.Char(
        string='NMID',
        readonly='True',
        help='National Merchant ID untuk QRIS harus ditampilkan dibawah QR pada layar atau cetakan QRIS jika menggunakan aplikasi / software / web.'
    )

    qris_invoice_request_date = fields.Char(
        string='Request Date',
        readonly='True',
        help='Request date sejak permintaan invoice dikirimkan ke QRIS'
    )

    def qris_api_get_create_invoice(self,passparams):
        url = "https://qris.id/restapi/qris/show_qris.php"
        response = requests.get(url, params=passparams)
        res = response.json()
        vals = {
            'api_provider' : 'QRIS',
            'api_prodivder_link' : url,
            'api_method' : 'get',
            'params' : str(passparams),
            'response' : str(res),
            'description' : 'Create QRIS Invoice'
        }
        self.env['unitek.api.history'].create(vals)
        return res

    def convert_qris_string_to_base64img(qris_string):
        qrisimg = qrcode.make(qris_string)
        buffered = BytesIO()
        qrisimg.save(buffered,'JPEG')
        qrisbase64 = base64.b64encode(buffered.getvalue())
        # raise UserError(str(type(qrisimg))+" AND "+str(type(qrisbase64)))
        return qrisbase64
        # TypeError: a bytes-like object is required, not 'PilImage'

    def tes_convert_img(self):
        self.qris_image = unitek_qris_model.convert_qris_string_to_base64img(self.qris_image_string)

    def qris_create_invoice(self):
        passparamsvar = {
            'do':'create-invoice',
            'apikey': self.env.company.qris_api_key,
            'mID':self.env.company.qris_mid,
            'cliTrxNumber':self.name,
            'cliTrxAmount': int(round(self.amount_residual))
        }
        res = unitek_qris_model.qris_api_get_create_invoice(self,passparamsvar)
        if res['status']=='success':
            res = res['data']
            self.qris_image_string=res['qris_content']
            self.qris_invoice_id=res['qris_invoiceid']
            self.qris_invoice_request_date=res['qris_request_date']
            self.qris_nmid=res['qris_nmid']
            self.qris_image = unitek_qris_model.convert_qris_string_to_base64img(self.qris_image_string)
        elif res['status']=='failed':
            self.qris_invoice_id=str(res['data'])

    def qris_api_get_check_invoice(self,passparams):
        url = "https://qris.id/restapi/qris/checkpaid_qris.php"
        response = requests.get(url, params=passparams)
        res = response.json()
        vals = {
            'api_provider' : 'QRIS',
            'api_prodivder_link' : url,
            'api_method' : 'get',
            'params' : str(passparams),
            'response' : str(res),
            'description' : 'Check QRIS Invoice have been paid or not'
        }
        self.env['unitek.api.history'].create(vals)
        return res

    # @api.depends('env.company')
    def qris_check_invoice(self):
        passparamsvar = {
            'do':'checkStatus',
            'apikey': self.env.company.qris_api_key,
            'mID':self.env.company.qris_mid,
            'invid':self.qris_invoice_id,
            'trxvalue':int(round(self.amount_residual)),
            'trxdate':self.qris_invoice_request_date[:10]
        }
        res = unitek_qris_model.qris_api_get_check_invoice(self,passparamsvar)
        if res['status']=='success':
            res = res['data']
            self.qris_status_paid=res['qris_status']
            self.qris_status_paid_by_customer=res['qris_payment_customername']
            self.qris_status_paid_by_platform=['qris_payment_methodby']
        if res['status']=='failed':
            res = res['data']
            self.qris_status_paid=res['qris_status']

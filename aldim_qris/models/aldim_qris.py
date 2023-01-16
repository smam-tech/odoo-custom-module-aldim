from odoo import fields,models
import json
import requests
import qrcode
import time

class aldim_qris_model(models.Model):
    _inherit='sale.order'
    _description="Integration with QRIS"

    image_image = fields.Image(
        string='Gambar',
        readonly='True',
        help='Generated Image'
    )
    
    image_string = fields.Char(
        string='Gambar-Mentah',
        readonly='True',
        help='Generated String untuk gambar yang akan di generate, berasal dari API'
    )

    api_status_paid = fields.Char(
        string='Status Pembayaran',
        readonly='True',
        help='Status apakah sudah dibayar atau belum'
    )

    api_status_paid_by_customer = fields.Char(
        string='Dibayar Oleh',
        readonly='True',
        default='UNPAID',
        help='Receipt dibayar oleh siapa'
    )

    api_status_paid_by_platform = fields.Char(
        string='Dibayar Melalui',
        readonly='True',
        default='UNPAID',
        help='Receipt dibayar melalui platform'
    )

    api_invoice_id = fields.Char(
        string='ID Invoice QRIS',
        readonly='True',
        help='Nomor Transaksi QRIS yang berupa integer yang dapat digunakan untuk memeriksa status pembayaran QRIS'
    )

    api_nmid = fields.Char(
        string='NMID',
        readonly='True',
        help='National Merchant ID untuk QRIS harus ditampilkan dibawah QR pada layar atau cetakan QRIS jika menggunakan aplikasi / software / web.'
    )

    api_invoice_request_date = fields.Char(
        string='Request Date',
        readonly='True',
        help='Request date sejak permintaan invoice dikirimkan ke QRIS'
    )

    def qris_api_get_create_invoice(self,passparams):
        url = " https://qris.id/restapi/qris/show_qris.php"
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
        self.env['aldim.api.history'].create(vals)
        return res

    def qris_create_invoice(self):
        passparamsvar = {
            'do':'create-invoice',
            'apikey': self.company_id.qris_api_key,
            'mID':self.company_id.qris_mid,
            'cliTrxNumber':self.name,
            'cliTrxAmount':self.amount_total
        }
        res = aldim_qris_model.qris_api_get_create_invoice(self,passparamsvar)
        if res['status']=='success':
            res = res['data']
            self.image_string=res['qris_content']
            self.api_invoice_id=res['qris_invoiceid']
            self.api_invoice_request_date=res['qris_request_date']
            self.api_nmid=res['qris_nmid']
            self.image_image = qrcode.make(self.image_string)
        elif res['status']=='failed':
            self.api_invoice_id=str(res['data'])

    def qris_api_get_check_invoice(self,passparams):
        url = " https://qris.id/restapi/qris/checkpaid_qris.php"
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
        self.env['aldim.api.history'].create(vals)
        return res

    # @api.depends('company_id')
    def qris_check_invoice(self):
        passparamsvar = {
            'do':'checkStatus',
            'apikey': self.company_id.qris_api_key,
            'mID':self.company_id.qris_mid,
            'invid':self.api_invoice_id,
            'trxvalue':self.amount_total,
            'trxdate':self.api_invoice_request_date[:10]
        }
        res = aldim_qris_model.qris_api_get_check_invoice(self,passparamsvar)
        if res['status']=='success':
            res = res['data']
            self.api_status_paid=res['qris_status']
            self.api_status_paid_by_customer=res['qris_payment_customername']
            self.api_status_paid_by_platform=['qris_payment_methodby']
        if res['status']=='failed':
            res = res['data']
            self.api_status_paid=res['qris_status']

from odoo import fields,models,api
from . import midtransclient as midtrans
import base64

class unitek_midtrans_model(models.Model):
    _name ='unitek.midtrans'
    _description='Midtrans function API'

    midtrans_odoo_id = fields.Char(
        string='Odoo Document ID',
        readonly='True',
        help='Inside Odoo Document ID'
    )
    midtrans_order_id = fields.Char(
        string='Order ID',
        readonly='True',
        help='Midtrans Order ID, it is generated from your default document/model id'
    )

    midtrans_ammount = fields.Integer(
        string='Ammount',
        readonly='True',
        help='Midtrans payment ammount that need to be paid'
    )

    midtrans_status_payment = fields.Boolean(
        string='Paid Status',
        help='Status Payment',
        readonly='True'
    )

    def snap_init(self):
        snap = midtrans.Snap(
            is_production=False,
            server_key= self.env.company.midtrans_server_key,
            client_key= self.env.midtrans_auth_string
        )
        return snap

    
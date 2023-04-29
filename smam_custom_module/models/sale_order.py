from odoo import fields,models

class SMAM_Custom_Module(models.Model):
    _inherit='sale.order'
    _description="Perpanjangan form sales"

    keterangan_tambahan = fields.Char(
        string='Keterangan Tambahan',
        required=True,
        index=False,
        help='Keterangan Tambahan'
    )
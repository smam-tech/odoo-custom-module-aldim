from odoo import fields,models,api
from odoo.exceptions import UserError, ValidationError

class smam_material(models.Model):
    _name = "smam.material"
    _description = "Material"

    smam_material_code = fields.Char(
        string='Material Code',
        required=True,
        help='Provider API yang mengirimkan Response'
    )

    smam_name = fields.Char(
        string='Material Name',
        required=True,
        help='Link Provider API yang mengirimkan Response'
    )

    smam_type = fields.Selection(
        string='Material Type',
        required=True,
        help='What the api call function',
        selection = [('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton','Cotton')]
    )

    smam_buy_price = fields.Float(
        string='Material Buy Price',
        help='Method to call the API',
        required=True,
    )

    smam_supplier = fields.Many2one(
        comodel_name='res.partner',
        string='Related Supplier',
        help='Tanggal Penerimaan Response',
        required=True,
    )

    @api.onchange('smam_buy_price')
    def check_buyp_more_100(self):
        for record in self:
            if record.smam_buy_price < 100 and record.smam_buy_price != False:
                raise UserError("Buy Price Value must be 100 or more")
            

    def download_report_excel(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/smam_material/excel_report/%s' % (self.id),
            'target': 'new',
        }

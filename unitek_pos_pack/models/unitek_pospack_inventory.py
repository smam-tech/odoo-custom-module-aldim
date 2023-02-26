from odoo import models, fields

class MyModel(models.Model):
    _inherit = 'product.template'

    available_in_pos = fields.Boolean(default=True)
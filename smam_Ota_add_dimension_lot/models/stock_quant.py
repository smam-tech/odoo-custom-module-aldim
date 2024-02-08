from itertools import chain

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import format_datetime
from odoo.tools.misc import formatLang, get_lang

class SMAMStockMoveRequest1(models.Model):
    _inherit = "stock.quant"

    smam_panjang = fields.Float(
        string='Panjang',
        help='Multiplier for done',
        digits=(12,3),
    )
    smam_tebal = fields.Float(
        string='Tebal',
        digits=(12,3),
        help='Multiplier for done'
    )
    smam_lebar = fields.Float(
        string='Lebar',
        digits=(12,3),
        help='Multiplier for done'
    )
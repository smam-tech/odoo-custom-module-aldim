from itertools import chain

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import format_datetime
from odoo.tools.misc import formatLang, get_lang

class SMAMRatePricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    #Field for the rate
    smam_rate = fields.Float(
        string='Rate',
        required=True,
        index=False,
        default=1,
        help='Rate which current price will be multiplied'
    )


    #Calculating rate, this function from original odoo function
    def _compute_price(self, price, price_uom, product, quantity=1.0, partner=False):
        price = super(SMAMRatePricelistItem, self)._compute_price(price, price_uom, product, quantity, partner)
        if self.compute_price == 'formula':
            if self.smam_rate:
                price = price * self.smam_rate
        return price
        
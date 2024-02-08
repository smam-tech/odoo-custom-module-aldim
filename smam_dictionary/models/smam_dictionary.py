from odoo import fields,models
from datetime import datetime
import time

class smam_dictionary(models.Model):
    _name = "smam.dictionary"
    _description = "For storing multiple dictionary stuff so you can show it on xml"

    key = fields.Char(
        string='Key',
        help='Key'
    )

    val_int = fields.Integer(
        string='Integer Value',
        help='Value in Integer Format'
    )

    val_str = fields.Char(
        string='String Value',
        help='Value in String Format'
    )

    val_monetary = fields.Monetary(
        string='Monetary Value',
        help='Value in Monetary (Money format)'
    )
from odoo import fields,models,api
from odoo.exceptions import UserError

class unitek_midtrans_accountmove_model(models.Model):
    _inherit='account.move'
    _description='Invoice Extend for midtrans'

    midtrans_redirect_url=fields.Char(
        string='Redirect URL',
        readonly='True',
        help='Midtrans payment amount that need to be paid',
        compute= '_compute_redirect_url'
    )

    midtrans_id=fields.Many2one(
        'unitek.midtrans',
        string='Midtrans',
        readonly='True',
        help='Midtrans record that connected'
    )

    def check_midtrans_transaction_paid(self):
        for invoice in self:
            # get status of transaction that already recorded on midtrans (already `charge`-ed)
            if invoice.midtrans_id:
                self.env['unitek.midtrans'].check_midtrans_transaction(invoice,invoice.midtrans_id)
            else :
                raise UserError("Midtrans Invoice Not Created yet, seriously what did you expect for me to check?")

    def create_midtrans_transaction(self):
        for invoice in self:
            if int(invoice.amount_residual)==0:
                return
            args = {
                "transaction_details":{
                    "order_id": invoice.name,
                    "gross_amount": invoice.amount_residual
                }
            }
            new_midtrans_id = self.env['unitek.midtrans'].create_midtrans_snap_transaction(
                invoice,
                invoice.name,
                args
            )
            invoice.midtrans_id = new_midtrans_id
    
    def create_redirect_midtrans_transaction(self):
        print("Idk man, iam being called here")
        return {
        'type': 'ir.actions.act_url',
        'url': self.midtrans_redirect_url,
        'target': 'new',
        }

    @api.depends('state')
    def _compute_redirect_url(self):
        for invoice in self:
            if invoice.state == "posted":
                if invoice.midtrans_id:
                    invoice.midtrans_redirect_url=invoice.midtrans_id.midtrans_redirect_url
                else:
                    invoice.create_midtrans_transaction()
                    invoice.midtrans_redirect_url=invoice.midtrans_id.midtrans_redirect_url
            else:
                invoice.midtrans_redirect_url=""


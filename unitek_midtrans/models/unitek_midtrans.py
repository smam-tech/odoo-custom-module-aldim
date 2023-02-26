from odoo import fields,models,api
from . import midtransclient as midtrans
import base64
from decimal import Decimal, ROUND_HALF_UP
from odoo.exceptions import UserError
#raise UserError('bruh')

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
        # readonly='True',
        help='Midtrans Order ID, it is generated from your default document/model id'
    )

    midtrans_amount = fields.Integer(
        string='amount',
        readonly='True',
        help='Midtrans payment amount that need to be paid'
    )

    midtrans_token = fields.Char(
        string='Token',
        readonly='True',
        help='Snap token for opening the Snap popup (https://snap-docs.midtrans.com/#overview12)'
    )

    midtrans_redirect_url = fields.Char(
        string='Redirect URL',
        readonly='True',
        help='Midtrans payment amount that need to be paid'
    )

    midtrans_status_payment = fields.Char(
        string='Paid Status',
        help='Status Payment',
        readonly='True',
        default='Not Paid'
    )

    def snap_init(self,passself=""):
        if passself != "":
            snap = midtrans.Snap(
                is_production=self.env.company.midtrans_is_production,
                server_key= self.env.company.midtrans_server_key,
                client_key= self.env.company.midtrans_auth_string
            )
            return snap
        else:
            snap = midtrans.Snap(
                is_production=passself.env.company.midtrans_is_production,
                server_key= passself.env.company.midtrans_server_key,
                client_key= passself.env.company.midtrans_auth_string
            )
            return snap
    
    def core_init(self,passself=""):
        if passself != "":
            core = midtrans.CoreApi(
                is_production=self.env.company.midtrans_is_production,
                server_key= self.env.company.midtrans_server_key,
                client_key= self.env.company.midtrans_auth_string
            )
            return core
        else:
            core = midtrans.CoreApi(
                is_production=passself.env.company.midtrans_is_production,
                server_key= passself.env.company.midtrans_server_key,
                client_key= passself.env.company.midtrans_auth_string
            )
            return core
    
    def conv_toint_half_up(ininteger):
        ininteger = Decimal(ininteger).to_integral_value(rounding=ROUND_HALF_UP)
        return int(ininteger)

    def convert_to_midtrans_order_id(instring):
        instring = instring.replace("/",".")
        return instring

    def status_code_translate(strstatuscode):
        if strstatuscode == '200':
            return "Success"
        elif strstatuscode == '201':
            return "Pending/Challange, Please check your MAP and search the Order ID"
        elif strstatuscode == '202':
            return "Denied"
        elif strstatuscode == '300':
            return "Move permanently. All current and future requests should be directed to the new URL permanently.Please create new invoice"
        elif strstatuscode == '400':
            return "Validation Error. You have sent bad request data like invalid transaction type, invalid payment card format, and so on."
        elif strstatuscode == '401':
            return "Access denied due to unauthorized transaction. Please check Client Key or Server Key."
        elif strstatuscode == '402':
            return "No access for this payment type."
        elif strstatuscode == '403':
            return "The requested resource is not capable of generating content in the format specified in the request headers."
        elif strstatuscode == '404':
            return "The requested resource/transaction is not found. Please check order_id or other details sent in the request."
        elif strstatuscode == '405':
            return "HTTP method is not allowed."
        elif strstatuscode == '406':
            return "Duplicate order ID. order_id has already been utilized previously."
        elif strstatuscode == '407':
            return "Expired transaction."
        elif strstatuscode == '408':
            return "Wrong data type."
        elif strstatuscode == '409':
            return "You have sent too many transactions for the same card number."
        elif strstatuscode == '410':
            return "Your account is deactivated. Please contact Midtrans support."
        elif strstatuscode == '411':
            return "token_id is missing, invalid, or timed out."
        elif strstatuscode == '412':
            return "You cannot modify status of the transaction."
        elif strstatuscode == '413':
            return "The request cannot be processed due to syntax error in the request body."
        elif strstatuscode == '414':
            return "Refund request is rejected due to merchant insufficient funds."
        elif strstatuscode == '429':
            return "API rate limit exceeded. The global rate limit is applied to Create Pay Account API and Charge API"
        elif strstatuscode == '500':
            return "Internal Server Error."
        elif strstatuscode == '501':
            return "The feature is not available."
        elif strstatuscode == '502':
            return "Internal Server Error: Bank Connection Problem."
        elif strstatuscode == '503':
            return "Bank/partner is experiencing connection issue."
        elif strstatuscode == '504':
            return "Internal Server Error: Midtrans Fraud Detection System is unavailable."
        elif strstatuscode == '505':
            return "Failure to create requested VA number. Try again later."
        elif strstatuscode == None:
            return "Status code not found, pls check API history"
        else:
            return "Unrecognizebale Status Code, pls check API history"

    def check_midtrans_transaction(self,passself,midtrans_row):
        core = unitek_midtrans_model.core_init(self,passself=passself)
        status = core.transactions.status(midtrans_row.midtrans_order_id)
        midtrans_row.midtrans_status_payment = unitek_midtrans_model.status_code_translate(str(status.get("status_code")))
        vals = {
            'api_provider' : 'Midtrans',
            'api_prodivder_link' : "https://app.midtrans.com/snap/v1/transactions",
            'api_method' : 'post',
            'params' : "Order ID :" + str(midtrans_row.midtrans_order_id),
            'response' : str(status),
            'description' : 'Check Midtrans Payment for Doc ID' + str(midtrans_row.midtrans_order_id)
        }
        self.env['unitek.api.history'].create(vals)

    
    def create_midtrans_snap_transaction(self,passself,strdocname,args):
        args['transaction_details']['order_id'] = unitek_midtrans_model.convert_to_midtrans_order_id(args['transaction_details']['order_id'])
        args['transaction_details']['gross_amount'] = unitek_midtrans_model.conv_toint_half_up(args['transaction_details']['gross_amount'])
        snap = unitek_midtrans_model.snap_init(self,passself=passself)
        res = snap.create_transaction(args)
        midtrans_id = None
        vals = {
            'api_provider' : 'Midtrans',
            'api_prodivder_link' : "https://app.midtrans.com/snap/v1/transactions",
            'api_method' : 'post',
            'params' : str(args),
            'response' : str(res),
            'description' : 'Create Midtrans for Doc ID' + str(strdocname)
        }
        self.env['unitek.api.history'].create(vals)
        if 'redirect_url' and 'token' in res.keys():
            midtrans_model_vals = {
                'midtrans_odoo_id':strdocname,
                'midtrans_order_id':args['transaction_details']['order_id'],
                'midtrans_amount':args['transaction_details']['gross_amount'],
                'midtrans_redirect_url':res["redirect_url"],
                'midtrans_token':res["token"]
            }
            midtrans_id = self.env['unitek.midtrans'].sudo().create(midtrans_model_vals)
        else:
            raise UserError(unitek_midtrans_model.status_code_translate(res.get("status_code")))
        return midtrans_id


    
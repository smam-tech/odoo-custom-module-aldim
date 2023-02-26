from odoo import http
from odoo.http import request

class CustomPostAPIMidtrans(http.Controller):
    @http.route('/api/custom/post', type='json', auth='public', methods=['POST'], csrf=False)
    def custom_post_api(self, **kwargs):
        # Access data from the POST request body
        data = request.jsonrequest
        print("\n\n\n\n\n\n\n\n\n\n")
        print(str(data))
        print("\n\n\n\n\n\n\n\n\n\n")
        return {'message': 'Success'}
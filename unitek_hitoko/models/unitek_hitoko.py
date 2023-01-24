from odoo import fields,models
import json
import requests
import hmac
import hashlib
import binascii

class UnitekHitoko(models.Model):
    _name = "unitek.hitoko"
    _description = "Hitoko Integration"

    def generate_signature_hitoko(self,passself,requestparams):
        client_id = passself.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_id_hitoko')
        access_token = passself.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.access_token_hitoko')
        client_secret = passself.env['ir.config_parameter'].sudo().get_param('unitek_hitoko.client_secret_hitoko')
        data = client_id + access_token + requestparams
        # Create a new HMAC object
        hmac_obj = hmac.new(client_secret, data, hashlib.sha256)

        # Get the digest of the data
        digest = hmac_obj.digest()

        # Convert the digest to a hex encoded string
        hex_encoded_digest = binascii.hexlify(digest)

        return hex_encoded_digest.decode()
    

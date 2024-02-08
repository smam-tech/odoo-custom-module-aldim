from odoo.tests import common

class TestSMAMMaterial(common.TransactionCase):
        
    def setUp(self):
        super(TestSMAMMaterial, self).setUp()
        self.partner = self.env['res.partner'].create({'name': 'Aldi Mulyawan'})
    
    def test_smam_mat(self):
        partner = self.env['res.partner'].create({'name': 'SMAM'})
        record = self.env['smam.material'].create({
            'smam_material_code': '007',
            'smam_name': 'Kain Bagus',
            'smam_type': 'fabric',
            'smam_buy_price': 600,
            'smam_supplier': partner.id,
        })
        self.assertEqual(record.smam_name, 'Kain Bagus')
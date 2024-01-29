from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Voyage Model class
class TestTransModell(models.TransientModel):
    _name = "test.trans.modell"
    _description = "test_trans_modell"
    name = fields.Char(string="NomVG", tracking=True)

    def action_test_trans(self):
        print("Button clicked:Lunching Action")
        action = self.env.ref("contact_travel.action_voyage").read()[0]
        return action

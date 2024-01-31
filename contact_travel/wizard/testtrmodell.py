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
        #orm create
        self.env["voyage"].create({'name':'TestORMCREATE','montant':456.8,'voyageur_id':3})
        #orm browse
        res=self.env["voyage"].browse([10,28])
        for rec in res:
            print(rec.name,rec.montant)
        #orm write
        res = self.env["voyage"].browse([19])
        if res.exists():
            res.write({'name':'mohamed'})
        #orm unlink
        res = self.env["voyage"].browse([19])
        if res.exists():
            res.unlink()
        #orm search
        res=self.env["voyage"].search([('name','=',"mohamed")])
        for rec in res:
            print(rec.id,rec.name,rec.montant)
        #orm search_count
        res = self.env["voyage"].search_count([('name', '=', "mohamed")])
        print(res)
        #orm fields_get
        res=self.env["voyage"].fields_get([('name','montant'),('type','string')])
        print(res)
        #orm metadata
        res=self.env["voyage"].browse([28])
        print(res.get_metadata())


        return action

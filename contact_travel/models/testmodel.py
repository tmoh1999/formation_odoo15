from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "namet"
    datebirth=fields.Date(string="Date of birth", default=fields.Date.context_today)
    namet=fields.Char(string="NameT",tracking=True)
    prdescription=fields.Text(string="Description")

    email=fields.Char(string="email")
    phone=fields.Char(string="phone")

    testnb=fields.Integer(string="Nbtest")
    testhtmlf=fields.Html(string="TestHTmlField")

    priority=fields.Selection([
        ("0","normal"),
        ("1","low"),
        ("2","High"),
        ("3","Very High"),
    ],String="Priority")

    stbar=fields.Selection([
        ("started","Started"),
        ("running","Running"),
        ("stopped","Stopped"),
        ("done","Done"),
    ],String="States",default="started",required=True)

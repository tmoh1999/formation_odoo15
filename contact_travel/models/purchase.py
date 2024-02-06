from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Contact Model class inherit from res.partner Model
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    hide_active = fields.Boolean(string="hide_active", default=True)

    @api.onchange('hide_active')
    def onchange_partner_id(self):
        print("Changed")

    def action_quotation_send_s(self):
        return


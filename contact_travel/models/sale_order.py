from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Contact Model class inherit from res.partner Model
class SaleOrder(models.Model):
    _inherit = "sale.order"
    hide_active = fields.Boolean(string="hide_active", default=True)
    def action_quotation_send_s(self):
        return


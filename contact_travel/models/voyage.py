import datetime

from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Voyage Model class 
class Voyage(models.Model):
    _name = "voyage"
    _description = "Voyage"
    _inherit = ["mail.thread","mail.activity.mixin"]

    @api.model
    def default_get(self,fields):
        res= super(Voyage,self).default_get(fields)
        res["montant"]=20980.9
        return res

    #Voyage Model Class attributes
    name= fields.Char(string="Nom du Voyage",tracking=True)
    dateDepart=fields.Datetime(string="Date de départ", default=fields.Datetime.now)
    destination=fields.Char(string="Destination")
    refv = fields.Char(string="Reference",read_only=True)
    montant=fields.Float(string="Montant Voyage",default=1234.0,required=True)
    active=fields.Boolean(string="Active",default="True")
    image=fields.Image(string="Image")
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company)

    currency_id = fields.Many2one('res.currency', string='Account Currency' ,related="company_id.currency_id")
    monfield=fields.Monetary(string="MonField",default=199.9)





    _sql_constraints = [
        ('name','unique(name)','Voyage Name must be unique')
    ]
    @api.constrains('dateDepart')
    def _(self):
        for record in self:
            if record.dateDepart:
                if record.dateDepart.year!=datetime.date.today().year:
                    raise ValidationError(_("Wrong Year in field datePart."))





    #Many2one attribute : a link between res.partner Model and Voyage Model 
    #res.partner Contact can have a list of voyages .     
    voyageur_id=fields.Many2one('res.partner', string='Contact',required=True)
    voyageur_phone = fields.Char(related="voyageur_id.phone")
    image2 = fields.Image(related="voyageur_id.image_1920")

    testmodel_id=fields.Many2one("test.model",string="TestModelRef")



    # The method create override the default version
    ## to call <caclNivRecompense> method to change the <nivrecompense> 
    ## of the related res.partner contact based on conditions.
      
    @api.model
    def create(self, vals):
        self.caclNivRecompense(vals)
        vals["refv"]=self.env['ir.sequence'].next_by_code('voyage')
        res=super(Voyage,self).create(vals)
        return res

    def write(self, vals):
        if "montant" in vals.keys():
            vals["voyageur_id"]=self.voyageur_id.id
            self.caclNivRecompense(vals)

        res=super(Voyage,self).write(vals)
        return res
    # Method caclNivRecompense  takes as input a list of tuples
    ## correspend to the result after the creation of the voyage.
    # And calculates the sum of the <montant> of each voyages related to the user
    ## plus to the new created <montant> value.
    # After that based on the total sum and the rules it calculates and changes the value
    ## of the <nivrecompense> of the related res.partner contact.
    
    def caclNivRecompense(self, vals):
        field_voy_contact = self.env['voyage'].search([('voyageur_id','=', vals["voyageur_id"])])
        
        mont_glob=vals["montant"]
        for vg in field_voy_contact:

            if not self.id or self.id!=vg.id:
                #print(vg.id, vg.montant, self.id)
                mont_glob+=vg.montant

            
        recomp=""
        if mont_glob>=100000:
            recomp= "platin"
        elif mont_glob>=50000:   
            recomp= "or"
        elif mont_glob>=20000:
            recomp= "argent"

        self.env['res.partner'].search([('id','=',vals["voyageur_id"])]).nivrecompense=recomp
        
    def name_get(self):
        return  [(record.id,"%s:%s" %(record.refv,record.name)) for record in self]

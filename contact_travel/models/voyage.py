from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Voyage Model class 
class Voyage(models.Model):
    _name = "voyage"
    _description = "Voyage"
    _inherit = ["mail.thread","mail.activity.mixin"]
    #Voyage Model Class attributes 
    name= fields.Char(string="Nom du Voyage",tracking=True)
    dateDepart=fields.Datetime(string="Date de départ", default=fields.Datetime.now)
    destination=fields.Char(string="Destination")
    refv = fields.Char(string="Reference")
    montant=fields.Float(string="Montant Voyage")
    active=fields.Boolean(string="Active",default="True")
    image=fields.Image(string="Image")


    
    #Many2one attribute : a link between res.partner Model and Voyage Model 
    #res.partner Contact can have a list of voyages .     
    voyageur_id=fields.Many2one('res.partner', string='Contact')
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
            mont_glob+=vg.montant
            
        recomp=""
        if mont_glob>=100000:
            recomp= "platin"
        elif mont_glob>=50000:   
            recomp= "or"
        elif mont_glob>=20000:
            recomp= "argent"
            
        self.env['res.partner'].search([('id','=',vals["voyageur_id"])]).nivrecompense=recomp
        
            
    
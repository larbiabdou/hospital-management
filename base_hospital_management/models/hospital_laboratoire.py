from odoo import models, fields

class MedicamentLaboratoire(models.Model):
    _name = 'medicament.laboratoire'
    _description = 'Laboratoire'

    name = fields.Char(string='Nom')
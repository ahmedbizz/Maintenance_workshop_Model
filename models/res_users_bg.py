from odoo import fields, models


class Users(models.Model):
    _inherit = 'res.users'

    name = fields.Char(string="")
    departmet_ids = fields.Many2many('department.bg', string='Department')
   
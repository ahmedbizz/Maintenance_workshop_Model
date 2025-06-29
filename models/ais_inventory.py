from odoo import api, fields, models, Command
from odoo.exceptions import ValidationError


class INVENTORY_All(models.Model):
    _name = "inventory.all"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "WorkShop INVENTORY"

    name = fields.Char(string="Catogery", translate=True, required=True)
    departmet_ids_inv = fields.Many2one('department.bg', string='Department', required=True)
    Sequence = fields.Char(string="Sequence")
# categ_id = fields.Selection([
# 	('0', 'Store'),
# 	('1', 'AIS'),
# 	('2', 'SAGM'),
# 	('3', 'FLIER')], string="Sequence",required=True)


class AIS_INVENTORY(models.Model):
    _name = "ais.inventory"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "WorkShop AIS INVENTORY"

    ref_pro = fields.Char(string="Refrance")
    name = fields.Char(string="Device Name", tracking=True, translate=True, required=True)
    PART_NO = fields.Char(string="PART NO", required=True)
    Location = fields.Char(string="Location", required=True)
    QTY_pro = fields.Integer(string='QTY', required=True)
    imge = fields.Image(string="Image")
    categ_ids = fields.Many2one('inventory.all', string='Catogery', required=True)
    Sequence_cat = fields.Char(string="Sequence")

    @api.onchange('categ_ids')
    def onchange_progress(self):
        for rec in self:
            self.Sequence_cat = rec.categ_ids.Sequence

    @api.constrains('QTY_pro')
    def _check_QTY_pro(self):
        for record in self:
            if record.QTY_pro < 0:
                raise ValidationError("Fields QTY_pro must be grater than 0")

    @api.model
    def create(self, vals):
        if vals['Sequence_cat']:
            ref_pro = vals['Sequence_cat'] + str(self.env['ir.sequence'].next_by_code('ais.inventory.All'))
            vals['ref_pro'] = ref_pro
        return super(AIS_INVENTORY, self).create(vals)


class ENTER_INVENTORY_PART(models.Model):
    _name = "enter.inventory.part"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "WorkShop ENTER INVENTORY Part"
    _rec_name = "technician_Engineer"

    date_IN_WorkShop = fields.Date(string='DATE ENTERING', tracking=True)
    file_scan_rep = fields.Binary(string='Report', attachment=True, tracking=True)
    file_scan_polisa = fields.Binary(string='Polisa', attachment=True, tracking=True)
    technician_Engineer = fields.Many2one('res.users', string='Engineer')
    technician_Manger = fields.Many2one('res.users', string='Manger', tracking=True)
    inv_pro_ids = fields.One2many('enter.inventory', 'send_ent_pro_id', string='PART')
    progress = fields.Selection([
        ('new', 'NEW'),
        ('request', 'Request ENTERING'),
        ('enter', 'ENTERING TO STORE'), ], default="new", string="progress", required=True, tracking=True)

    def action_request_entering(self):
        for rec in self:
            rec.progress = "request"
            rec.technician_Engineer = self.env.user.id

    def action_confirm_part(self):
        for rec in self:
            for line in rec.inv_pro_ids:
                line.ref_ve_pro()
        rec.progress = "enter"
        rec.technician_Manger = self.env.user.id


class REQ_INVENTORY_PART(models.Model):
    _name = "req.inventory.part"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "WorkShop REQUEST INVENTORY Part"

    date_IN_WorkShop = fields.Date(string='DATE OUT', tracking=True)
    file_scan_rep = fields.Binary(string='Report', attachment=True, tracking=True)
    file_scan_polisa = fields.Binary(string='Polisa', attachment=True, tracking=True)
    technician_Engineer = fields.Many2one('res.users', string='Engineer')
    inv_pro_ids = fields.One2many('enter.inventory', 'send_req_pro_id', string='PART')
    progress = fields.Selection([
        ('new', 'NEW'),
        ('req', 'REQUESTED'), ], default="new", string="progress", required=True, tracking=True)

    def action_req_part(self):
        for rec in self:
            for line in rec.inv_pro_ids:
                line.in_ve_pro()
        rec.progress = "req"
        rec.technician_Engineer = self.env.user.id


class ENTER_INVENTORY(models.Model):
    _name = "enter.inventory"
    _description = "WorkShop ENTER INVENTORY"

    name_part = fields.Many2one('ais.inventory', string='Part Name', required=True, tracking=True)
    ref = fields.Char(string='ref', related="name_part.ref_pro", tracking=True)
    PART_NO = fields.Char(string="PART NO.", related="name_part.PART_NO", tracking=True)
    QTY = fields.Integer(string='QTY', related="name_part.QTY_pro", tracking=True)
    reuect_num = fields.Integer(string="RQUECT", required=True, tracking=True)
    send_ent_pro_id = fields.Many2one('enter.inventory.part')
    send_req_pro_id = fields.Many2one('req.inventory.part')

    def in_ve_pro(self):
        for rec in self.name_part:
            if (rec.QTY_pro - self.reuect_num) >= 0:
                rec.QTY_pro = rec.QTY_pro - self.reuect_num
            else:
                raise ValidationError("Field QTY must be grater than 0")

    def ref_ve_pro(self):
        for rec in self.name_part:
            if self.reuect_num >= 0:
                rec.QTY_pro = rec.QTY_pro + self.reuect_num
            else:
                raise ValidationError("Field QTY must be grater than 0")

# @api.model
# def create(self,vals):
# 	ref_pro = ''
# 	if vals['categ_id'] == '0':
# 		ref_pro = self.env['ir.sequence'].next_by_code('ais.inventory.All')
# 	elif vals['categ_id'] == '1':
# 		ref_pro = self.env['ir.sequence'].next_by_code('ais.inventory')
# 	elif vals['categ_id'] == '2':
# 		ref_pro = self.env['ir.sequence'].next_by_code('ais.inventory.sagem')
# 	elif vals['categ_id'] == '3':
# 		ref_pro = self.env['ir.sequence'].next_by_code('ais.inventory.Flier')
# 	vals['ref_pro'] = ref_pro
# 	return super(AIS_INVENTORY, self).create(vals)

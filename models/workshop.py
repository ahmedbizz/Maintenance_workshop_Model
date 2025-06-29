from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime,  date, timedelta


class DepartmentBg(models.Model):
    _name = "department.bg"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Workshop Department"

    name = fields.Char(string="Workshop Name")
    Sequence = fields.Char(string="Sequence")


class WORKSHOP_SENDRECEIVED(models.Model):
    _name = "workshop.sendreceived"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "WorkShop SEND & RECEIVED"
    _rec_name = "name_id"

    ref = fields.Char(string="REFERENCE")
    name_id = fields.Many2one('ais.inventory', string="DEVICE NAME", tracking=True, required=True)
    SERIAL_NO = fields.Char(string="SERIAL NO.", required=True, tracking=True)
    date_IN_WorkShop = fields.Date(string='DATE ENTERING', tracking=True)
    ExpireDateWarranty = fields.Date(string='Warranty Expire In', tracking=True)
    QTY = fields.Integer(string='QTY', default=1, required=True, tracking=True)
    days = fields.Integer(string='Days',required=True)
    ISSUE_NOTE = fields.Html(string='ISSUE/NOTE', required=True, tracking=True)
    STATUS = fields.Selection([
        ('new', 'Check'),
        ('fexied', 'REPAIRED'),
        ('replacing', 'REPLACEMENT'),
        ('destruction', 'DESTRUCTION'),
        ('Projection', 'Projection'),
        ('pendig', 'Waiting for spare parts'),
        ('confirm', 'Confirm Spar Part'),
        ('reject', 'Reject Spar Part'),
        ('send_new', 'Send New Part'),
        ('Request_send_new', 'Request send new PART'),
        ('Request_replacement', 'Request replacement'),
        ('Request_stored', 'Request stored'),
        ('stored', 'STORED'),
        ('expire','Warranty expired'),
        ('valid','Valid warranty'),
        ('sent_com','Sent to the company'),
        ('renewed','Repaired and warranty renewed')],
        default="new", string="STATUS", tracking=True)
    REPAIR_ACTION = fields.Html(string='REPAIR ACTION', tracking=True)
    Description = fields.Html(string='Description', tracking=True)
    DATE_OUT = fields.Date(string='DATE OUT', tracking=True)
    active = fields.Boolean(string="active", default=True, tracking=True)
    REGION = fields.Selection([
        ('riyadh', 'RIYADH'),
        ('jeddah', 'JEDDAH'),
        ('abha', 'ABHA'),
        ('yanbu', 'YANBU'),
        ('jizan', 'JIZAN'),
        ('damam', 'DAMAM'),
        ('asir', 'asir'),
        ('najran', 'najran'),
        ('aljouf', 'aljouf'),
        ('MAKKAH', 'Makkah  almukarama'),
        ('Madinah', 'AL Madinah AL Munawwarah'),
        ('shargiya', 'ashargiya'),
        ('SHUMALIYA', 'SHUMALIYA'),
        ('tabuk', 'TABUK')], string='REGION', tracking=True)
    sector = fields.Selection([
        ('Tabuk', 'Tabuk'),
        ('alqida', 'AL-QIADA'),
        ('almudirya', 'AlMudirya- riyadh'),
        ('halat eamaar', 'halat eamaar'),
        ('haql', 'haql'),
        ('albadae', 'Duba'),
        ('Duba', 'Tabuk'),
        ('alwajh', 'alwajh'),
        ('amlaj', 'amlaj'),
        ('Tabuk Training Center', 'Tabuk Training Center'),
        ('Fahd base', 'Fahd base'),
        ('Eastern', 'Eastern'),
        ('Arada', 'Arada'),
        ('Batha', 'Batha'),
        ('Salwa', 'Salwa'),
        ('alkhabar', 'alkhabar'),
        ('Qatif', 'Qatif'),
        ('Hafar Al-Batin', 'Hafar Al-Batin'),
        ('Jubail', 'Jubail'),
        ('Khafji', 'Khafji'),
        ('Ras Tanura', 'Ras Tanura'),
        ('Abdulaziz Port', 'Abdulaziz Port'),
        ('wahdat alhimaya', 'wahdat alhimaya'),
        ('Eastern Training Center', 'Eastern Training Center'),
        ('Naif base', 'Naif base'),
        ('North', 'North'),
        ('alshueba', 'alshueba'),
        ('Rafha', 'Rafha'),
        ('Al-Awiqila', 'Al-Awiqila'),
        ('aljadida', 'aljadida'),
        ('tarif', 'tarif'),
        ('Northern Training Center', 'Northern Training Center'),
        ('aljawf', 'aljawf'),
        ('alhaditha', 'alhaditha'),
        ('Al-Issawiya', 'Al-Issawiya'),
        ('Tabuk', 'Tabuk'),
        ('halat eamaar', 'halat eamaar'),
        ('haql', 'haql'),
        ('albadae', 'albadae'),
        ('Duba', 'Duba'),
        ('alwajh', 'alwajh'),
        ('amlaj', 'amlaj'),
        ('Tabuk Training Center', 'Tabuk Training Center'),
        ('Fahd base', 'Fahd base'),
        ('AL Madinah AL Munawwarah', 'AL Madinah AL Munawwarah'),
        ('Yanbu Commercial Port', 'Yanbu Commercial Port'),
        ('Yanbu Commercial Port', 'Yanbu Commercial Port'),
        ('Yanbu Industrial Port', 'Yanbu Industrial Port'),
        ('mina almuejiz', 'mina almuejiz'),
        ('quat almarakiz alshamalia', 'quat almarakiz alshamalia'),
        ('quat almarakiz aljanubia', 'quat almarakiz aljanubia'),
        ('Makkah  almukarama', 'Makkah  almukarama'),
        ('Rabigh', 'Rabigh'),
        ('jida', 'jida'),
        ('Laith', 'Laith'),
        ('Qunfudhah', 'Qunfudhah'),
        ('Jeddah Por', 'Jeddah Por'),
        ('Aramco port', 'Aramco port'),
        ('Marine force', 'Marine force'),
        ('Mohammed base', 'Mohammed base'),
        ('easir', 'easir'),
        ('alqahma', 'alqahma'),
        ('zahran aljanub', 'zahran aljanub'),
        ('Jazan', 'Jazan'),
        ('Pesh', 'Pesh'),
        ('almawsim', 'almawsim'),
        ('fursan', 'fursan'),
        ('altiwal', 'altiwal'),
        ('alharth', 'alharth'),
        ('alearida', 'alearida'),
        ('aldaayir', 'aldaayir'),
        ('Jazan port', 'Jazan port'),
        ('Ahmed base', 'Ahmed base'),
        ('Najran', 'Najran'),
        ('suqam', 'suqam'),
        ('kubash', 'kubash'),
        ('sharura', 'sharura'),
        ('metco', 'metco / FLIER'),
        ('arar', 'ARAR'),
        ('mazra', 'MAZRA'),
        ('BAESHA', 'BARSHA'),
        ('AVIATION', 'AVIATION AFFAIRS'),
        ('ISTIQBARATH', 'ISTIQBARATH'),
        ('Intelligence', 'Intelligence')], string='SECTOR', tracking=True)
    kan_prog_col = fields.Selection([
        ('new', 'NEW'),
        ('IN', 'IN progress'),
        ('sper', 'Request spare parts'),
        ('confirm', 'Confirm'),
        ('Projection', 'Projection'),
        ('reject', 'Reject'),
        ('done', 'DONE'),
        ('send', 'SEND'),
        ('stored', 'STORED')], default="new", string="progress", required=True, tracking=True)
    progress = fields.Selection([
        ('new', 'NEW'),
        ('IN', 'IN progress'),
        ('sper', 'Request spare parts'),
        ('confirm', 'Confirm'),
        ('Projection', 'Projection'),
        ('reject', 'Reject'),
        ('done', 'DONE'),
        ('send', 'SEND'),
        ('send_new', 'Send New Part'),
        ('Request_send_new', 'Request Send New Part'),
        ('stored', 'STORED'),
        ('Request_replacement', 'Request Replacement'),
        ('Request_stored', 'Request Stored'),
        ('replacing', 'REPLACEMENT'),
        ('expire', 'Warranty expired'),
        ('valid', 'Valid warranty'),
        ('sent_com', 'Sent to the company'),
        ('renewed', 'Repaired and warranty renewed'),
        ('7_days', '7 Days warranty expired'),
    ], default="new", string="progress", required=True, tracking=True)
    technician_id = fields.Many2one('res.users',required=True,string='Technician',
                                    tracking=True)
    technician_Engineer = fields.Many2one('res.users', string='Engineer', tracking=True)
    technician_Manger = fields.Many2one('res.users', string='Manger', tracking=True)
    inv_pro_ids = fields.One2many('spar.part', 'send_res_pro_id', string='SPAR')
    file_scan_rep = fields.Binary(string='Report', attachment=True, tracking=True)
    file_scan_polisa = fields.Binary(string='Polisa', attachment=True, tracking=True)
    req_count = fields.Integer(compute="_compute_req", store=True, tracking=True)
    imge = fields.Image(string="Image", related="name_id.imge", tracking=True)
    color = fields.Integer('Color Index', default=0)
    Departmet_ids = fields.Many2one('department.bg', string='Department', required=True, tracking=True)
    Departmet_id = fields.Char(srting="dep", translate=True)
    Sequence_cat = fields.Char(string="Sequence Tiket")
    Warranty = fields.Selection([
        ('7_days', '7 Days warranty expired'),
        ('expire', 'Warranty expired'),
        ('valid', 'Valid warranty'),
        ('sent_com', 'Sent to the company'),
        ('renewed', 'Repaired and warranty renewed')],
         string="Warranty", tracking=True)
    Warranty_Part_list = fields.One2many('warranty.part', 'send_res_warranty', string='Warranty Part')
    def ExpireDate(self):
        num =1
        user =self.search([])
        data =self.env['warranty.part'].search([])
        for rec in user:
            for lin in data:
                if self.SERIAL_NO == lin.SERIAL_NO and self.name_id.name == lin.name.name:
                    rec.Warranty = lin.Warranty
            if rec.ExpireDateWarranty:
                rec.days =int((rec.ExpireDateWarranty - datetime.today().date()).days)
                if rec.days == 173 :
                    rec.Warranty = "7_days"
                if datetime.today().date() >= rec.ExpireDateWarranty:
                    rec.Warranty = "expire"
                else:
                    rec.Warranty = 'valid'



    @api.onchange('Departmet_ids')
    def onchange_Departmet_ids(self):
        for rec in self:
            self.Sequence_cat = rec.Departmet_ids.Sequence
    @api.depends('SERIAL_NO')
    def onchange_SERIAL_NO(self):
        data =self.env['warranty.part'].search([])
        for rec in self:
            for lin in data:
                if rec.SERIAL_NO == lin.SERIAL_NO:
                    rec.Warranty = lin.Warranty
                    rec.ExpireDateWarranty = lin.ExpireDateWarranty
                    rec.ExpireDate()

    @api.constrains('QTY')
    def _check_QTY(self):
        for record in self:
            if record.QTY <= 0:
                raise ValidationError("Fields QTY must be grater than 0")

    def _compute_req(self):
        for rec in self:
            rec.req_count = self.env['workshop.sendreceived'].search_count([('name_id', '=', rec.name_id.name)])


    @api.constrains('SERIAL_NO')
    def _check_SERIAL_NO(self):
        data = self.env['workshop.sendreceived'].search([
            ('name_id', '=', self.name_id.name),
            ('SERIAL_NO','=',self.SERIAL_NO),
            ('id', '!=', self.id),
             ('progress', 'in', ('IN','sper','confirm','Projection','reject','done','send_new','Request_send_new','new','Request_replacement','replacing','expire','7_days','renewed'))])
        if data:
            raise ValidationError("There is already Ticket open it is not close yet !!")

    @api.model
    def create(self, vals):
        if vals['Sequence_cat']:
            ref_pro = vals['Sequence_cat'] + str(self.env['ir.sequence'].next_by_code('workshop.sendreceived'))
            vals['ref'] = ref_pro
        self.ExpireDate()
        return super(WORKSHOP_SENDRECEIVED, self).create(vals)



    def action_done(self):
        for rec in self:
            rec.progress = "done"
            rec.STATUS = "fexied"
            rec.technician_Engineer = self.env.user.id

    def SentCompany(self):
        for rec in self:
            rec.progress = "sent_com"
            rec.Warranty = "sent_com"
            rec.ExpireDateWarranty = ''
            rec.days = ''
            rec.technician_Engineer = self.env.user.id

    def renewedWarnty(self):
        for rec in self:
            rec.progress = "renewed"
            rec.Warranty = "renewed"
            data = self.env['warranty.part'].search([('SERIAL_NO','=',self.SERIAL_NO),('name', '=', self.name_id.name)])
            for lin in data:
                lin.ExpireDateWarranty =datetime.today().date() + timedelta(days=180)
                rec.ExpireDateWarranty=datetime.today().date() + timedelta(days=180)
            rec.ExpireDate()
            rec.technician_Engineer = self.env.user.id


    def action_replacing(self):
        for rec in self:
            for line in rec.name_id:
                if line.QTY_pro >= 0:
                    line.QTY_pro -= self.QTY
                    rec.technician_Manger = self.env.user.id
                else:
                    raise ValidationError("No stock available")
            rec.progress = "replacing"
            rec.STATUS = "replacing"
            rec.technician_Manger = self.env.user.id

    def your_method(self): 
        purchase_group = self.env.ref('AIS_WORKSHOP.group_workshop_Soldier')
        purchase_user = self.env['res.users'].search([('groups_id', '=', purchase_group),])
        notification_ids = []
        for purchase in purchase_user:
            notification_ids.append((0,0,{
                'res_partner_id':purchase.partner_id.id,
                'notification_type':'inbox'}))
        self.message_post(body='This receipt has been validated!'
                , message_type='notification'
                , subtype='mail.mt_comment'
                , author_id='self.env.user.partner_id.id'
                , notification_ids=notification_ids)
  
    def action_Projection(self):
        for rec in self:
            rec.progress = "Projection"
            rec.STATUS = "Projection"
            rec.technician_Engineer = self.env.user.id


    def action_IN(self):
        test = self.env['res.users'].search([])
        user = self.env['workshop.sendreceived'].search([('name_id','=',self.name_id.name),('SERIAL_NO','=',self.SERIAL_NO)])
        data =self.env['warranty.part'].search([('name','=',self.name_id.name),('SERIAL_NO','=',self.SERIAL_NO)])

        if self.Departmet_ids.name == 'AIS':
            self.technician_Engineer =self.env['res.users'].search([('login','=','ahmed-50-@hotmail.com')])
            self.technician_Manger = self.env['res.users'].search([('login', '=', 'safran.alotaibi@gmail.com')])
        if self.Departmet_ids.name == 'SAGEM':
            self.technician_Engineer =self.env['res.users'].search([('login','=','moayad.84@gmail.com')])
            self.technician_Manger = self.env['res.users'].search([('login', '=', 'bander@workshop.com')])
        if self.Departmet_ids.name == 'CCTV':
            self.technician_Engineer =self.env['res.users'].search([('login','=','mnaveedanwar233@gmail.com')])
            self.technician_Manger = self.env['res.users'].search([('login', '=', 'alrznah.f@gmail.com')])
        if self.Departmet_ids.name == 'FLIER':
            self.technician_Engineer = self.env['res.users'].search([('login', '=', 'dheensha16@gmail.com')])
            self.technician_Manger = self.env['res.users'].search([('login', '=', 'safran.alotaibi@gmail.com')])
        if data:
            for rec in user:
                for lin in data:
                    if rec.SERIAL_NO == lin.SERIAL_NO:
                        rec.Warranty = lin.Warranty
                        rec.ExpireDateWarranty = lin.ExpireDateWarranty
                        self.progress = "IN"

                    else:
                        self.progress = "IN"
        else:
            self.progress = "IN"
        self.ExpireDate()



    def action_req_replac(self):
        for rec in self:
            rec.progress = "Request_replacement"
            rec.STATUS = "Request_replacement"
            rec.technician_Engineer = self.env.user.id


    def action_sper(self):
        for rec in self:
            rec.progress = "sper"
            rec.STATUS = "pendig"


    def action_confirm(self):
        for rec in self:
            if self.inv_pro_ids:
                for line in rec.inv_pro_ids:
                    if line.conf != 'confirm':
                        line.in_ve_pro()
            else:
                raise ValidationError("Wait For Engineer to add Parts")
            rec.progress = "confirm"
            rec.STATUS = "confirm"
            rec.technician_Manger = self.env.user.id


    def action_print(self):
        return self.env.ref('AIS_WORKSHOP.workshop_spar_print_badge').report_action(self)


    def action_report(self):
        return self.env.ref('AIS_WORKSHOP.workshop_sendreceived_print_badge').report_action(self)


    def action_reject(self):
        for rec in self:
            rec.progress = "reject"
            rec.STATUS = "reject"
            rec.technician_Manger = self.env.user.id


    def action_send(self):
        for rec in self:
            rec.progress = "send"
            rec.technician_Engineer = self.env.user.id


    def action_send_new(self):
        for rec in self:
            for line in rec.name_id:
                if line.QTY_pro >= 0:
                    line.QTY_pro -= self.QTY
                    rec.technician_Manger = self.env.user.id
                else:
                    raise ValidationError("No stock available")
            rec.progress = "send_new"
            rec.STATUS = "send_new"
            rec.technician_Manger = self.env.user.id


    def action_req_send_new(self):
        for rec in self:
            rec.progress = "Request_send_new"
            rec.STATUS = "Request_send_new"
            rec.technician_Engineer = self.env.user.id


    def action_stored(self):
        for rec in self:
            for line in rec.name_id:
                line.QTY_pro += self.QTY
            rec.progress = "stored"
            rec.STATUS = "stored"
            rec.technician_Manger = self.env.user.id


    def action_req_stored(self):
        for rec in self:
            rec.progress = "Request_stored"
            rec.STATUS = "Request_stored"
            rec.technician_Engineer = self.env.user.id


class Spar_Part(models.Model):
    _name = "spar.part"
    _description = "spart part"

    name = fields.Many2one('ais.inventory', string='Part Name', required=True, tracking=True)
    ref = fields.Char(string='ref', related="name.ref_pro", tracking=True)
    PART_NO = fields.Char(string="PART NO.", related="name.PART_NO", tracking=True)
    conf = fields.Char(string="Confirmation", tracking=True)
    QTY = fields.Integer(string='QTY', related="name.QTY_pro", tracking=True)
    reuect_num = fields.Integer(string="RQUECT", required=True, tracking=True)
    send_res_pro_id = fields.Many2one('workshop.sendreceived')

    @api.constrains('reuect_num')
    def _check_reuect_num(self):
        for record in self:
            if record.reuect_num <= 0:
                raise ValidationError("Fields RQUECT must be grater than 0")

    def in_ve_pro(self):
        for rec in self.name:
            if (rec.QTY_pro - self.reuect_num) >= 0:
                rec.QTY_pro = rec.QTY_pro - self.reuect_num
                self.conf = 'confirm'
            else:
                raise ValidationError("Field QTY must be grater than 0")

    def ref_ve_pro(self):
        for rec in self.name:
            if self.reuect_num >= 0:
                rec.QTY_pro = rec.QTY_pro + self.reuect_num
            else:
                raise ValidationError("Field QTY must be grater than 0")
class Warranty_Part(models.Model):
    _name = "warranty.part"
    _description = "Warranty Part"

    name = fields.Many2one('ais.inventory', string='Part Name', required=True, tracking=True)
    ref = fields.Char(string='ref', related="name.ref_pro", tracking=True)
    PART_NO = fields.Char(string="PART NO.", related="name.PART_NO", tracking=True)
    QTY = fields.Integer(string='QTY', related="name.QTY_pro", tracking=True)
    SERIAL_NO = fields.Char(string="SERIAL NO.", required=True, tracking=True)
    Days_warranty = fields.Integer(string="Days warranty",  tracking=True)
    send_res_warranty = fields.Many2one('workshop.sendreceived')
    ExpireDateWarranty = fields.Date(string='Warranty Expire In', tracking=True)
    Departmet_Warranty_ids = fields.Many2one('department.bg', string='Department', required=True, tracking=True)
    Warranty = fields.Selection([
        ('7_days', '7 Days warranty expired'),
        ('expire', 'Warranty expired'),
        ('valid', 'Valid warranty'),
        ('sent_com', 'Sent to the company'),
        ('renewed', 'Repaired and warranty renewed')],
         string="Warranty", tracking=True)
    def ExpireDate(self):
        num =1
        user =self.search([])
        for rec in user:
            if rec.ExpireDateWarranty:
                rec.Days_warranty = int((rec.ExpireDateWarranty - datetime.today().date()).days)
                if rec.Days_warranty == 173 :
                    rec.Warranty = "7_days"
                if datetime.today().date() >= rec.ExpireDateWarranty:
                    rec.Warranty = "expire"
                else:
                    rec.Warranty = 'valid'
    @api.constrains('SERIAL_NO')
    def _check_SERIAL_NO(self):
        data = self.env['warranty.part'].search([('SERIAL_NO','=',self.SERIAL_NO),('name','=',self.name.name),('id', '!=', self.id)])
        if data:
            raise ValidationError("This Device is already Add Can not Duple it  !!")

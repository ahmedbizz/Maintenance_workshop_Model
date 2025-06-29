from odoo import api, fields, models, Command
from odoo.exceptions import ValidationError
from datetime import datetime

class EmployeeMetco(models.Model):
    _name = "employee.metco"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "MTECO STUFF"

    name = fields.Char(string="Employee Name",required=True)
    emp_ID = fields.Char(string="Employee ID",required=True)
    email = fields.Char(string="Employee ID", required=True)
    phone_no = fields.Char(string="phone")
    imge = fields.Image(string="Image")
    emp_scan_ID = fields.Binary(string='Iqama/ID', required=True,attachment=True, tracking=True)
    emp_scan_passport = fields.Binary(string='Passport',required=True, attachment=True, tracking=True)
    DATE_EXP_TS = fields.Date(string='DATE PERMIT',tracking=True)
    DATE_HAIER = fields.Date(string='HAIER DATE',required=True, tracking=True)
    Departmet_ids = fields.Many2one('department.bg',required=True, string='Department')
    REGION = fields.Selection([
        ('riyadh','RIYADH'),
        ('jeddah','JEDDAH'),
        ('abha','ABHA'),
        ('yanbu','YANBU'),
        ('jizan','JIZAN'),
        ('damam','DAMAM'),
        ('asir','asir'),
        ('najran','najran'),
        ('aljouf','aljouf'),
        ('MAKKAH','Makkah  almukarama'),
        ('Madinah','AL Madinah AL Munawwarah'),
        ('shargiya','ashargiya'),
        ('SHUMALIYA','SHUMALIYA'),
        ('tabuk','TABUK')], string='REGION',tracking=True,required=True)
    sector = fields.Selection([
        ('Tabuk','Tabuk'),
        ('halat eamaar','halat eamaar'),
        ('haql','haql'),
        ('albadae','Duba'),
        ('Duba','Tabuk'),
        ('alwajh','alwajh'),
        ('amlaj','amlaj'),
        ('Tabuk Training Center','Tabuk Training Center'),
        ('Fahd base','Fahd base'),
        ('Eastern','Eastern'),
        ('Arada','Arada'),
        ('Batha','Batha'),
        ('Salwa','Salwa'),
        ('alkhabar','alkhabar'),
        ('Qatif','Qatif'),
        ('Hafar Al-Batin','Hafar Al-Batin'),
        ('Jubail','Jubail'),
        ('Khafji','Khafji'),
        ('Ras Tanura','Ras Tanura'),
        ('Abdulaziz Port','Abdulaziz Port'),
        ('wahdat alhimaya','wahdat alhimaya'),
        ('Eastern Training Center','Eastern Training Center'),
        ('Naif base','Naif base'),
        ('North','North'),
        ('alshueba','alshueba'),
        ('Rafha','Rafha'),
        ('Al-Awiqila','Al-Awiqila'),
        ('aljadida','aljadida'),
        ('tarif','tarif'),
        ('Northern Training Center','Northern Training Center'),
        ('aljawf','aljawf'),
        ('alhaditha','alhaditha'),
        ('Al-Issawiya','Al-Issawiya'),
        ('Tabuk','Tabuk'),
        ('halat eamaar','halat eamaar'),
        ('haql','haql'),
        ('albadae','albadae'),
        ('Duba','Duba'),
        ('alwajh','alwajh'),
        ('amlaj','amlaj'),
        ('Tabuk Training Center','Tabuk Training Center'),
        ('Fahd base','Fahd base'),
        ('AL Madinah AL Munawwarah','AL Madinah AL Munawwarah'),
        ('Yanbu Commercial Port','Yanbu Commercial Port'),
        ('Yanbu Commercial Port','Yanbu Commercial Port'),
        ('Yanbu Industrial Port','Yanbu Industrial Port'),
        ('mina almuejiz','mina almuejiz'),
        ('quat almarakiz alshamalia','quat almarakiz alshamalia'),
        ('quat almarakiz aljanubia','quat almarakiz aljanubia'),
        ('Makkah  almukarama','Makkah  almukarama'),
        ('Rabigh','Rabigh'),
        ('jida','jida'),
        ('Laith','Laith'),
        ('Qunfudhah','Qunfudhah'),
        ('Jeddah Por','Jeddah Por'),
        ('Aramco port','Aramco port'),
        ('Marine force','Marine force'),
        ('Mohammed base','Mohammed base'),
        ('easir','easir'),
        ('alqahma','alqahma'),
        ('zahran aljanub','zahran aljanub'),
        ('Jazan','Jazan'),
        ('Pesh','Pesh'),
        ('almawsim','almawsim'),
        ('fursan','fursan'),
        ('altiwal','altiwal'),
        ('alharth','alharth'),
        ('alearida','alearida'),
        ('aldaayir','aldaayir'),
        ('Jazan port','Jazan port'),
        ('Ahmed base','Ahmed base'),
        ('Najran','Najran'),
        ('suqam','suqam'),
        ('kubash','kubash'),
        ('sharura','sharura'),
        ('metco','metco / FLIER'),
        ('arar','ARAR'),
        ('mazra','MAZRA'),
        ('BAESHA','BARSHA'),
        ('AVIATION','AVIATION AFFAIRS'),
        ('ISTIQBARATH','ISTIQBARATH'),
        ('Intelligence','Intelligence')], string='SECTOR',tracking=True)
    Warranty = fields.Selection([
        ('7_days', '7 Days Permit expired'),
        ('expire', 'Permit expired'),
        ('valid', 'Valid Permit')],
         string="Permit", tracking=True)
    days = fields.Integer(string='Days', default=1, required=True, tracking=True)

    def ExpireDatePrmit(self):
        user =self.search([])
        for rec in user:
            if rec.DATE_EXP_TS:
                rec.days =int((rec.DATE_EXP_TS - datetime.today().date()).days)
                if rec.days <= 10 :
                    rec.Warranty = "7_days"
                if datetime.today().date() >= rec.DATE_EXP_TS:
                    rec.Warranty = "expire"
                else:
                    rec.Warranty = "valid"

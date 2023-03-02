from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval

class record(models.Model):
    _name = 'record.teacher'
    _description = 'All records of the student'
    _rec_name = 'Teacher_Name'

    Teacher_Name = fields.Char(string='Teacher Name')
    Subject_Name = fields.Char(string='Subject')
    Lec_No = fields.Integer(string='Lecture Number')
    Section_Name = fields.Char(string='Section')
    Time = fields.Integer(string='Time')
    department = fields.Char(string='Department')
    batch_no = fields.Char(string='Batch_No')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="gender")


    #student Records








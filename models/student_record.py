from odoo import fields, api, models, _
from odoo.exceptions import ValidationError





class data(models.Model):

    _name = 'lib.staff'
    _description = 'record of data'
    _rec_name = 'name'



    #onchange
    # @api.onchange('Semster','Batch_No')
    # def _onchange_Semster(self):
    #     # set auto-changing field
    #     self.price = self.amount * self.unit_price
    #     # Can optionally return a warning and domains
    #     return {
    #         'warning': {
    #             'title': "Something bad happened",
    #             'message': "It was very bad indeed",
    #         }
    #     }

    #Validation Error

    @api.constrains('age')
    def val_age(self):
        for record in self:
            if int(record.age) < 18:
                raise ValidationError("your age is less then 18: %s" % record.age)


    #Basic Info Feilds
    name = fields.Char(string='Student Name')
    age = fields.Char(string="Student Age")
    dob = fields.Date(string="Student DOB")
    Number = fields.Integer(string='Student Contact')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="gender")
    #new field add
    status = fields.Selection([('active', 'Active'), ('shutdown', 'Shutdown')], string="status")
    Section = fields.Char(string="Student Section")

    #Additional Information Fields
    mobile = fields.Char(string="Student Mobile")
    email = fields.Char(string="Student Email")
    state = fields.Char(string="states")
    department = fields.Char(string="Student Department")
    Semester = fields.Char(string="Student Semester")
    Batch_No = fields.Char(string="Student Batch_NO")
    time = fields.Float(string='Time')
    Date = fields.Date(string='Date')
    photo = fields.Binary(string='Student Image')
    country_id = fields.Many2many('res.country',string='Country')




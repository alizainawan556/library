from odoo import fields, models


class  newlib(models.Model):
    _name = 'new.lib'
    _description = 'books record'

    name = fields.Char(string='Name of book')
    title = fields.Char(string='Title')
    price = fields.Integer(string='Price')
    notes = fields.Text(string='Notes')
    image = fields.Image()
    release_date = fields.Date(string='Release Date')
    upload_date = fields.Date(string='Upload Date')

    partner_id = fields.Many2many('res.partner', string='Authors')
    partner_city = fields.Char(string='Partner city', related='partner_id.city')


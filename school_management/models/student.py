

from odoo import models, fields


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student Table'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    guardian = fields.Char(string="Guardian")
    note = fields.Text(string="Note")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')
    image = fields.Binary(string="Image")





from odoo import models, fields


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student Table'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    grade = fields.Integer(string='Grade')
    guardian = fields.Char(string="Guardian")
    note = fields.Text(string="Note")
    section = fields.Selection([
        ('lp', 'LP'),
        ('up', 'UP'),
        ('hs', 'HS')
    ], string='Section', default='lp')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')
    image = fields.Binary(string="Image")



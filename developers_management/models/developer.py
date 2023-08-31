# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime


class Developer(models.Model):
    _name = "developer"
    _description = 'Developers'

    name = fields.Char(string="Name", copy=False, require=True)
    type = fields.Selection(
        selection=[
            ('front-end', 'Front-end'),
            ('backend', 'Backend'),
            ('fullstack', 'Full Stack'),
            ('out-stuff', 'Out Stuff')
        ],
        string='Developer Type',
    )
    global_identification = fields.Char(string="Global Identification", compute="_compute_global_identification")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")
    date_of_birth = fields.Date(string="Date of Birth")
    company_id = fields.Many2one(comodel_name="res.company", string="Company")

    _sql_constraints = [
        ('developer_name_uniq', 'unique(name)', 'Name for developers must be unique !'),
    ]

    @api.depends("name", "type")
    def _compute_global_identification(self):
        for developer in self:
            dev_name = developer.name or ""
            dev_type = developer.type or ""
            developer.global_identification = _("%s %s developer" % (dev_name, dev_type))

    @api.model
    def create(self, vals):
        if ('date_of_birth' in vals
                and vals['date_of_birth'] != False and datetime.strptime(vals['date_of_birth'],
                                                                         "%Y-%m-%d").date() > fields.Date.today()):
            vals['date_of_birth'] = fields.Date.today()
        return super().create(vals)

    def write(self, vals):
        if 'date_of_birth' in vals and vals['date_of_birth'] != False and datetime.strptime(vals['date_of_birth'],
                                                                                            "%Y-%m-%d").date() > fields.Date.today():
            vals['date_of_birth'] = fields.Date.today()
        return super().write(vals)

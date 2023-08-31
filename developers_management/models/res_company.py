# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = "res.company"

    developers = fields.One2many('developer', 'company_id', string='Developers')

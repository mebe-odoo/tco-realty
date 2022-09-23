# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date("Date of birth")
    place_of_birth = fields.Char("Place of birth")
    nationality = fields.Char("Nationality")

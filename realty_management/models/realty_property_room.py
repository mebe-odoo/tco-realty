# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RealtyPropertyRoom(models.Model):
    _name = 'realty.property.room'
    _description = 'Realty Property Room'

    name = fields.Char("Name", required=True)
    surface = fields.Float("Surface", default=0)
    property_id = fields.Many2one("realty.property")
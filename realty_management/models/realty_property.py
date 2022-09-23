# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RealtyProperty(models.Model):
    _name = 'realty.property'
    _description = 'Realty Property'

    name = fields.Char("Name", required=True)
    construction_date = fields.Date("Construction Date", required=True)

    company_id = fields.Many2one("res.company", default=lambda self: self.env.company)
    company_currency_id = fields.Many2one(string='Company Currency', related='company_id.currency_id', readonly=True)

    room_ids = fields.One2many("realty.property.room", "property_id", string="Rooms", required=True)
    tenancy_ids = fields.One2many("realty.tenancy", "property_id", string="Tenancy Contracts")

    rent = fields.Monetary("Rent", default=0.0, currency_field='company_currency_id', required=True)
    parking_spots = fields.Integer("Parking Spots", default=0)
    surface = fields.Float("Surface", default=0)

    is_furnished = fields.Boolean("Is Furnished", default=False)
    is_available = fields.Boolean("Available for Rent", compute="_compute_rent_status")
    is_rented = fields.Boolean("Is Rented", compute="_compute_rent_status")

    def _compute_rent_status(self):
        for property_id in self:
            # Solution 1: We query the realty_tenancy table by using the Search ORM method and passing a domain
            # This is usually more efficient than using filtered, if you have a large collection of records
            active_tenancies = self.env['realty.tenancy'].search([('state', '=', 'active'), ('id', 'in', property_id.tenancy_ids.ids)], limit=1)
            property_id.is_rented = bool(active_tenancies)
            # Solution 2: We use a the filtered ORM method to filter our tenancy_ids
            property_id.is_rented = bool(property_id.tenancy_ids.filtered(lambda t: t.state == 'active'))
            property_id.is_available = not property_id.is_rented

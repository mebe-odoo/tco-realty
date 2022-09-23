# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date


class RealtyTenancy(models.Model):
    _name = 'realty.tenancy.line'
    _description = 'Realty Tenancy Line'

    tenancy_id = fields.Many2one("realty.tenancy", string="Tenancy")
    property_id = fields.Many2one(related="tenancy_id.property_id")

    product_id = fields.Many2one("product.product", string="Product", domain=[('type', 'in', ('rent', 'charges'))])

    quantity = fields.Float("Quantity", default=1.0)
    price_unit = fields.Float(related="product_id.list_price", string="Price", store=True, readonly=False)

    amount_total = fields.Float("Total", compute="_compute_amount_total", store=True)

    @api.depends('price_unit', 'quantity')
    def _compute_amount_total(self):
        for line in self:
            line.amount_total = line.quantity * line.price_unit

    def action_click_me(self):
        pass
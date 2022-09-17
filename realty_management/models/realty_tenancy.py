# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date


class RealtyTenancy(models.Model):
    _name = 'realty.tenancy'
    _description = 'Realty Tenancy'

    name = fields.Char("Name", compute="_compute_tenancy_name")

    property_id = fields.Many2one("realty.property", required=True)
    tenant_ids = fields.Many2many("res.partner", string="Tenants")

    date_start = fields.Date("Start Date", required=True, default=date.today())
    date_end = fields.Date("End Date")

    state = fields.Selection([('draft', 'Draft'), ('active', 'Active'), ('cancel', 'Cancelled'), ('done', 'Terminated')], default='draft', string="State")

    tenancy_line_ids = fields.One2many("realty.tenancy.line", "tenancy_id", "Tenancy Lines")

    def name_get(self):
        result = []
        for tenancy in self:
            if tenancy.state == 'draft':
                result.append((tenancy.id, _("Draft Tenancy")))
            else:
                result.append((tenancy.id, tenancy.name))
        return result

    def _compute_tenancy_name(self):
        for tenancy in self:
            tenancy.name = tenancy.property_id.name
            if tenancy.id:
                tenancy.name += ' | ' + str(tenancy.id)

    def action_confirm(self):
        if self.state != 'draft':
            raise UserError(_("This tenancy has already been confirmed"))
        if not self.date_end or self.date_end < self.date_start:
            raise UserError(_("The End Date has to be set after the Start Date"))
        if not any(l.product_id.type == 'rent' for l in self.tenancy_line_ids):
            raise UserError(_("Set at least one Tenancy Line with a Rent product"))
        if not self.tenant_ids:
            raise UserError(_("Set at least one Tenant on your Tenancy"))
        self.state = 'active'

    def action_terminate(self):
        if self.state != 'active':
            raise UserError(_("You cannot terminate a tenancy that is not active"))
        self.state = 'done'

    def _cron_check_termination(self):
        tenancy_ids = self.search([('state', '=', 'active'), ('date_end', '<', date.today())])
        for tenancy in tenancy_ids:
            tenancy.action_terminate()

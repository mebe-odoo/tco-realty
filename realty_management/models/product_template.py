# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[('rent', 'Rent'), ('charges', 'Charges')], ondelete={
        'rent': 'set default',
        'charges': 'set default',
    })

    type = fields.Selection(selection_add=[('rent', 'Rent'), ('charges', 'Charges')])

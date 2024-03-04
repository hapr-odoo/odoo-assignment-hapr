# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class FleetCategory(models.Model):
    # _name = 'fleet.vehicle.model.category'
    _inherit = 'fleet.vehicle.model.category'
    _description = 'For list view of fleet categories'

    max_weight = fields.Integer(string='Max Weight (Kg)')
    max_volume = fields.Integer(string='Max Volume (m³)')

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} ({rec.max_weight}kg, {rec.max_volume}m³)"
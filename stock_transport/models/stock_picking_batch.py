# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from dateutil.relativedelta import relativedelta

class StockPickingBatchInherit(models.Model):
    _inherit = 'stock.picking.batch'
    _description = 'For form view of inventory batch'

    dock = fields.Many2one('dock', string='Dock')
    vehicle = fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    weight = fields.Float(string='Weight', compute='_compute_weight', store=True)
    volume = fields.Float(string='Volume', compute='_compute_volume', store=True)
    date_start = fields.Date(string='Start date', default=fields.Date.today())
    date_stop = fields.Date(string='End date', default=fields.Date.today()+relativedelta(days=4))

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} ({rec.weight}kg, {rec.volume}m³)"

    @api.onchange('picking_ids')
    def _compute_weight(self):
        total_weight = 0
        for rec in self.picking_ids:
            total_weight += (rec.shipping_weight)

        if self.vehicle_category.max_weight != 0:
            self.weight = (total_weight*100.0) / self.vehicle_category.max_weight
        else:
            self.weight = 0.01

    @api.onchange('picking_ids')
    def _compute_volume(self):
        total_volume = 0
        for rec in self.picking_ids:
            total_volume += (rec.volume_for_transfer)

        if self.vehicle_category.max_volume != 0:
            self.volume = (total_volume*100.0) / self.vehicle_category.max_volume
        else:
            self.volume = 0.01

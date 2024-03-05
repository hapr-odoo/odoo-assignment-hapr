# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'
    _description = 'For form view of transfers in inventory'

    volume_for_transfer = fields.Float(string='Volume', compute='_compute_volume', store=True)

    @api.depends('product_id.volume')
    def _compute_volume(self):
        for record in self:
            volumes = map(lambda move: move.product_id.volume * move.quantity, record.move_ids)
            record.volume_for_transfer = sum(volumes)
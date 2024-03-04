# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'
    _description = 'For form view of transfers in inventory'

    volume_for_transfer = fields.Float(string='Volume')

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Transport',
    'version': '1.0',
    'category': 'Dispatch Management System',
    'summary': 'A module for Dispatch Management System',
    'description': "This module, Dispatch Management System, is helpful in transport management system.",
    'depends': ['stock_picking_batch', 'fleet'],
    'data': [
        # "security/security.xml",
        "security/ir.model.access.csv",

        "views/fleet_category_list_view.xml",
        "views/inventory_batch_graph_view.xml",
        "views/inventory_batch_form_view.xml",
    ],
    'installable': True,
    'auto-install': True,
    'license': 'LGPL-3'
}

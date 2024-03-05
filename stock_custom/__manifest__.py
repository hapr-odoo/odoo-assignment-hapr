# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Custom',
    'version': '1.0',
    'category': 'Dispatch Management System',
    'summary': 'A custom module for Stock',
    'description': "This module automatically installs the Dispatch Management System.",
    'depends':[
        'stock'
    ],
    'data': [
        'views/res_config_view.xml'
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3'
}

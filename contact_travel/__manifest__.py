# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'contact_travel',
    'version': '1.0',
    'category': 'ContactTravel',
    'author' : 'TOUABTI Mohamed',
    'sequence': -100,
    'summary': 'Odoo Test Module',
    'description': """
Odoo Test Module.
    """,
    'depends':[
        'contacts',
        'mail',
    ],
    'data':[
        "security/ir.model.access.csv",
        "data/sequence_data.xml",
        "data/voyage_data.xml",
        "views/menu.xml",
        "views/voyage_view.xml",
        "wizard/testtrmodell.xml",
        "views/contact_view_inherit.xml",
        "views/test_model_view.xml"
    ],
    'demo':[],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license':'LGPL-3'
}

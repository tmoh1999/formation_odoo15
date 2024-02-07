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
        "sale",
        "purchase",
        "hr"
    ],
    'data':[
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/sequence_data.xml",
        "data/voyage_data.xml",
        "views/menu.xml",
        "views/voyage_view.xml",
        "wizard/testtrmodell.xml",
        "views/contact_view_inherit.xml",
        "views/test_model_view.xml",
        "data/email_template_data.xml",
        "report/report_voyage_card_template.xml",
        "report/report_inherite_hr_employe.xml",
        "report/report.xml",
        "views/sale_order_inherit.xml",
        "views/purchase_order_inherit.xml"
    ],
    'css':[
        "static/src/style.css",
    ],
    'demo':[],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license':'LGPL-3'
}

# -*- coding: utf-8 -*-
{
    'name': "Realty Management",

    'summary': """Realty Management App""",

    'description': """
        Realty Management App.
        Icon designed by Prosymbols and found on: https://www.flaticon.com/free-icons/town
    """,

    'author': "Mehdi Bendali Hacine (mebe@odoo.com)",
    'website': "https://odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/realty_property_views.xml',
        'views/realty_tenancy_views.xml',
        'views/res_partner_views.xml',
    ],
}

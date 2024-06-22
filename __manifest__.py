# -*- coding: utf-8 -*-
{
    'name': "custom/addons/account_invoince_whatsapp",
    'license': 'LGPL-3',

    'summary': """
        Send easy way invoice to whatsapp
        Now you can send yours invoice customer by whatsapp and download at there device""",

    'description': """
        customer could donwload the invoice in pdf format and send to whatsapp
    """,

    'author': "AR",
    'website': "http://www.taveras.com",


    # Categories can be used to filter modules in modules listing

    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/account_move_views.xml',
        'views/res_config_settings_view.xml',
        #'views/res_config_settings_view_tree.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': 'statics/images/icon.png',
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',

}

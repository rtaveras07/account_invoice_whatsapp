# -*- coding: utf-8 -*-
{
    'name': "Invoice WhatsApp",
    'license': 'LGPL-3',
    'summary': """Customer can download the invoice in PDF format and send it to WhatsApp""",
    'description': """
Send Invoices Easily via WhatsApp

Now you can effortlessly send invoices to your customers through WhatsApp! Follow these simple steps to ensure your customers can download and access their invoices directly on their devices:

1. **Create the Invoice:**
   - From odoo you create the invoice.
   - in the button send y print you can send the invoice to whatsapp from the button send via whatsapp.

2. **Save the Invoice as a PDF:**
   - the customer can download the invoice in PDF format through the link that is sent to WhatsApp.

3. **Before start to enjoy it:**
   - Create a Supabase account.
   - Create a new project. (storage)
   - in odoo Open Settings, Whatsapp Settings and complete the fields with the information of your supabase account.
   - comple the key, url and bucket of your supabase account.
   """,
    'author': "AR",
    'website': "http://ar.taveras.com.do",
    'category': 'Accounting',
    'version': '15.0.1.0.0',
    'depends': ['base', 'account'],
    'data': [
        'views/account_move_views.xml',
        'views/res_config_settings_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

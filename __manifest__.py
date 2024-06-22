# -*- coding: utf-8 -*-
{
    'name': "Invoince Whatsapp",
    'license': 'LGPL-3',

    'summary': """
        Send Invoices Easily via WhatsApp

Now you can effortlessly send invoices to your customers through WhatsApp! Follow these simple steps to ensure your customers can download and access their invoices directly on their devices:

    Create the Invoice:
        Use your preferred invoicing software or application to generate the invoice.
        Ensure the invoice includes all necessary details such as itemized charges, total amount, due date, and payment instructions.

    Save the Invoice as a PDF:
        Export or save the completed invoice as a PDF file.
        Make sure the PDF is clear and easily readable.

    Send the Invoice via WhatsApp:
        Open WhatsApp on your device.
        Select the customer you wish to send the invoice to from your contacts or start a new chat.
        Tap on the attachment icon (usually a paperclip) in the chat window.
        Choose the 'Document' option and select the PDF invoice from your files.
        Add a message if needed, then tap 'Send'.

    Customer Downloads the Invoice:
        The customer will receive the PDF invoice in their WhatsApp chat.
        They can tap on the PDF to open it.
        To download, they simply tap on the download button or use the options menu to save the PDF to their device.

By using WhatsApp for invoice delivery, you ensure quick and convenient access for your customers, enhancing their overall experience and streamlining your billing process.""",

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

        'views/account_move_views.xml',
        'views/res_config_settings_view.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    #'images': 'statics/images/icon.png',
    'icon': 'account_invoice_whatsapp/static/images/icon.png',
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',

}

import base64
import urllib.parse
from supabase import create_client, Client


from odoo import models, api

from datetime import datetime as dt


class AccountInvoiceSend(models.TransientModel):
    _name = 'account.invoice.send'
    _inherit = 'account.invoice.send'

    @api.model
    def action_send_whatsapp(self, additional_argument=None):
        # Obtain the current invoice
        invoice = self.env['account.move'].browse(self._context.get('active_id'))

        # Generate the PDF report of the invoice
        report = self.env.ref('account.account_invoices')
        pdf_data = report._render_qweb_pdf([invoice.id])[0]

        # Supabase configuration
        SUPABASE_URL = 'https://gfhxgswznpwkxoqujdln.supabase.co'
        SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdmaHhnc3d6bnB3a3hvcXVqZGxuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTg4OTk4NTAsImV4cCI6MjAzNDQ3NTg1MH0.ZfjrGWV1xwN1M-D5YoJQNsbJtSaYghTSSsdCBCQxhaM'
        SUPABASE_BUCKET = 'odooinvoices'

        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

        # Generate the filename
        current_time = dt.now().strftime("%Y%m%d_%H%M%S_%f")
        file_name = f"Factura_{current_time}_{invoice.name}.pdf"
        # Convert the PDF data to a base64 encoded string
        encoded_pdf_data = base64.b64encode(pdf_data).decode('utf-8')

        # Upload PDF to Supabase
        response = supabase.storage.from_(SUPABASE_BUCKET).upload(file_name, base64.b64decode(encoded_pdf_data), {
            'content-type': 'application/pdf'
        })

        public_url = f"https://gfhxgswznpwkxoqujdln.supabase.co/storage/v1/object/public/odooinvoices/{file_name}"

        # Prepare the WhatsApp message and phone number
        phone_number = '8299667478'
        whatsapp_message = f"¡Aquí está tu factura! Puedes ver y descargar el PDF de la factura en el siguiente enlace: {public_url}"

        # URL encode the message
        encoded_message = urllib.parse.quote(whatsapp_message)

        # Create the WhatsApp URL
        whatsapp_url = f"https://api.whatsapp.com/send?phone={phone_number}&text={encoded_message}"

        return {
            'type': 'ir.actions.act_url',
            'url': whatsapp_url,
            'target': 'new'
        }

import base64
import urllib.parse
from supabase import create_client, Client
from odoo import models, fields, api

from datetime import datetime as dt


class AccountInvoiceSend(models.TransientModel):
    _name = 'account.invoice.send'
    _inherit = 'account.invoice.send'
    #mobile = fields.Char(related='partner_id.mobile', string='Mobile', store=True)

    @api.model
    def action_send_whatsapp(self, additional_argument=None):


        # Obtain the current invoice
        invoice = self.env['account.move'].browse(self._context.get('active_id'))
        # Check if the mobile number is present
        phone_number = invoice.partner_id.mobile
        if not phone_number:
            # Fetch the partner record to complete the information
            partner = self.env['res.partner'].browse(invoice.partner_id.id)
            return {
                'type': 'ir.actions.act_window',
                'name': 'Error',
                'res_model': 'res.partner',
                'view_mode': 'form',
                'view_id': self.env.ref('base.view_partner_form').id,
                'target': 'new',
                'res_id': partner.id,
                'context': {
                    'default_message': 'No hay número de teléfono registrado para este cliente. Por favor, complete la información del cliente.'
                }
            }
        # Generate the PDF report of the invoice
        report = self.env.ref('account.account_invoices')
        pdf_data = report._render_qweb_pdf([invoice.id])[0]

        # Supabase configuration
        # Obtener la configuración de Supabase más reciente
        supabase_config = self.env['res.config.settings'].sudo().search([], order='id desc', limit=1)

        # Verificar si se encontró alguna configuración
        if not supabase_config:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Error',
                    'type': 'warning',
                    'message': 'No se encontró ninguna configuración de Supabase.'
                }
            }

        # Obtener los valores específicos de la configuración
        SUPABASE_URL = supabase_config.supabase_url
        SUPABASE_KEY = supabase_config.supabase_key
        SUPABASE_BUCKET = supabase_config.supabase_bucket

        # Aquí puedes continuar con tu lógica de negocio utilizando SUPABASE_URL, SUPABASE_KEY y SUPABASE_BUCKET

        # Por ejemplo, imprimir los valores obtenidos
        print(f"SUPABASE_URL: {SUPABASE_URL}")
        print(f"SUPABASE_KEY: {SUPABASE_KEY}")
        print(f"SUPABASE_BUCKET: {SUPABASE_BUCKET}")


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

        phone_number = invoice.partner_id.mobile

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

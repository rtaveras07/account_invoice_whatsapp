import base64
import requests
from odoo import models, api

class AccountInvoiceSend(models.TransientModel):
    _name = 'account.invoice.send'
    _inherit = 'account.invoice.send'

    @api.model
    def action_send_whatsapp(self, additional_argument=None):
        # Obtener la factura actual
        invoice = self.env['account.move'].browse(self._context.get('active_id'))

        # Generar el informe PDF de la factura
        report = self.env.ref('account.account_invoices')
        pdf_data = report._render_qweb_pdf([invoice.id])[0]

        # Codificar el contenido del PDF en base64
        pdf_content = base64.b64encode(pdf_data)

        # Copiar el PDF a Supabase
        supabase_url = 'https://api.supabase.io/storage/v1/upload'
        headers = {'Content-Type': 'application/octet-stream'}
        response = requests.post(supabase_url, headers=headers, data=pdf_data)
        if response.status_code != 200:
            return {'warning': {'title': 'Error', 'message': 'Error al cargar el archivo a Supabase.'}}

        # Obtener el enlace generado por Supabase para el archivo PDF
        pdf_url = response.json()['url']

        # Adjuntar el enlace al mensaje de WhatsApp
        phone_number = '18299667478'
        whatsapp_message = f"¡Aquí está tu factura! Descarga el PDF de la factura: {pdf_url}"

        whatsapp_url = f"https://api.whatsapp.com/send?phone={phone_number}&text={whatsapp_message}"

        return {
            'type': 'ir.actions.act_url',
            'url': whatsapp_url,
            'target': 'new'
        }

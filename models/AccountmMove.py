import base64
from odoo import models, fields, api


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
        pdf_content = base64.b64encode(pdf_data)

        # Adjuntar el PDF al mensaje de WhatsApp
        phone_number = '18299667478'
        whatsapp_message = f"¡Aquí está tu factura! Adjunto el PDF de la factura."

        whatsapp_url = f"https://api.whatsapp.com/send?phone={phone_number}&text={whatsapp_message}"
        whatsapp_url += f"&data=application/pdf;base64,{pdf_content.decode('utf-8')}"
        #copiar el pdf a supabase y enviar el link



        return {
            'type': 'ir.actions.act_url',
            'url': whatsapp_url,
            'target': 'new'
        }

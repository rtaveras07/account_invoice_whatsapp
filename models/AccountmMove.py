from odoo import models, fields, api

class AccountInvoiceSend(models.TransientModel):
    _name = 'account.invoice.send'
    _inherit = 'account.invoice.send'


    @api.model
    def action_send_whatsapp(self, additional_argument=None):
        whatsapp_url = f"https://api.whatsapp.com/send?phone=18299667478"
        #add pdf


        return {
            'type': 'ir.actions.act_url',
            'url': whatsapp_url,
            'target': 'new'
        }



from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    supabase_url = fields.Char(string="Supabase URL")
    supabase_key = fields.Char(string="Supabase Key")
    supabase_bucket = fields.Char(string="Supabase Bucket")

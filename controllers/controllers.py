# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/addons/invoicewhatsapp(http.Controller):
#     @http.route('/custom/addons/invoicewhatsapp/custom/addons/invoicewhatsapp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/addons/invoicewhatsapp/custom/addons/invoicewhatsapp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/addons/invoicewhatsapp.listing', {
#             'root': '/custom/addons/invoicewhatsapp/custom/addons/invoicewhatsapp',
#             'objects': http.request.env['custom/addons/invoicewhatsapp.custom/addons/invoicewhatsapp'].search([]),
#         })

#     @http.route('/custom/addons/invoicewhatsapp/custom/addons/invoicewhatsapp/objects/<model("custom/addons/invoicewhatsapp.custom/addons/invoicewhatsapp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/addons/invoicewhatsapp.object', {
#             'object': obj
#         })

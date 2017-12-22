# -*- coding: utf-8 -*-
from odoo import http

# class Modulex(http.Controller):
#     @http.route('/modulex/modulex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulex/modulex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulex.listing', {
#             'root': '/modulex/modulex',
#             'objects': http.request.env['modulex.modulex'].search([]),
#         })

#     @http.route('/modulex/modulex/objects/<model("modulex.modulex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulex.object', {
#             'object': obj
#         })
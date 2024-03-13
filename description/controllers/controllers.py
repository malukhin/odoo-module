# -*- coding: utf-8 -*-
# from odoo import http


# class Description(http.Controller):
#     @http.route('/description/description', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/description/description/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('description.listing', {
#             'root': '/description/description',
#             'objects': http.request.env['description.description'].search([]),
#         })

#     @http.route('/description/description/objects/<model("description.description"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('description.object', {
#             'object': obj
#         })

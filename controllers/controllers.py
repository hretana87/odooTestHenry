# -*- coding: utf-8 -*-
from odoo import http

# class Alquileres(http.Controller):
#     @http.route('/alquileres/alquileres/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alquileres/alquileres/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alquileres.listing', {
#             'root': '/alquileres/alquileres',
#             'objects': http.request.env['alquileres.alquileres'].search([]),
#         })

#     @http.route('/alquileres/alquileres/objects/<model("alquileres.alquileres"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alquileres.object', {
#             'object': obj
#         })
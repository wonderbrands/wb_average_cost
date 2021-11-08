# -*- coding: utf-8 -*-
from odoo import http

# class AverageCost(http.Controller):
#     @http.route('/wb_average_cost/wb_average_cost/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wb_average_cost/wb_average_cost/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wb_average_cost.listing', {
#             'root': '/wb_average_cost/wb_average_cost',
#             'objects': http.request.env['wb_average_cost.wb_average_cost'].search([]),
#         })

#     @http.route('/wb_average_cost/wb_average_cost/objects/<model("wb_average_cost.wb_average_cost"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wb_average_cost.object', {
#             'object': obj
#         })
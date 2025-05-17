# -*- coding: utf-8 -*-
# from odoo import http


# class SupplyChain(http.Controller):
#     @http.route('/supply_chain/supply_chain', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supply_chain/supply_chain/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('supply_chain.listing', {
#             'root': '/supply_chain/supply_chain',
#             'objects': http.request.env['supply_chain.supply_chain'].search([]),
#         })

#     @http.route('/supply_chain/supply_chain/objects/<model("supply_chain.supply_chain"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supply_chain.object', {
#             'object': obj
#         })


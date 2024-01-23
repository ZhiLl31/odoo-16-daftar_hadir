# -*- coding: utf-8 -*-
# from odoo import http


# class DaftarHadir(http.Controller):
#     @http.route('/daftar_hadir/daftar_hadir', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/daftar_hadir/daftar_hadir/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('daftar_hadir.listing', {
#             'root': '/daftar_hadir/daftar_hadir',
#             'objects': http.request.env['daftar_hadir.daftar_hadir'].search([]),
#         })

#     @http.route('/daftar_hadir/daftar_hadir/objects/<model("daftar_hadir.daftar_hadir"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('daftar_hadir.object', {
#             'object': obj
#         })

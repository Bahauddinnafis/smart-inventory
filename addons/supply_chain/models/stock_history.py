# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SmartInventoryHistory(models.Model):
    _name = "smart.inventory.history"
    _description = "Riwayat Stok Kustom"
    _order = "date desc"  # Urutkan berdasarkan tanggal terbaru

    product_id = fields.Many2one("smart.inventory", string="Produk", required=True)
    qty = fields.Float(string="Kuantitas", required=True)
    date = fields.Date(string="Tanggal", default=fields.Date.today(), required=True)
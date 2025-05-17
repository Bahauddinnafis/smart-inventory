# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SmartProduct(models.Model):
    _name = 'smart.inventory'
    _description = 'Manajemen Stok Cerdas'

    name = fields.Char(string='Nama Produk', required=True)
    current_stock = fields.Float(string='Stok Saat Ini', default=0)
    min_stock = fields.Float(string='Stok Minimum', default=10)
    supplier = fields.Char(string='Supplier')
    image = fields.Binary(string="Gambar Produk", attachment=True)
    
    # Demand Forecasting (Prediksi Permintaan)
    forecast_demand = fields.Float(string="Prediksi Permintaan", compute="_compute_forecast")
    history_stock = fields.One2many("smart.inventory.history", "product_id", string="Riwayat Stok")  # Relasi ke model kustom

    @api.depends("history_stock")
    def _compute_forecast(self):
        for product in self:
            last_3_months = product.history_stock[-3:] if product.history_stock else []
            total = sum(record.qty for record in last_3_months)  # Gunakan field qty dari model kustom
            product.forecast_demand = total / 3 if last_3_months else 0
            
    # Supplier Performance Dashboard
    supplier_rating = fields.Float(string="Rating Supplier (1-5)")
    last_delivery_time = fields.Integer(string="Lead Time (Hari)")
    
    # Peringatan stok rendah
    @api.model
    def check_stock(self):
        products = self.search([])
        for product in products:
            if product.current_stock < product.min_stock:
                self.env['mail.thread'].message_post(
                    body=f"Stok {product.name} tersisa {product.current_stock}! Segera pesan ke {product.supplier}.",
                    subject='Peringatan Stok Rendah'
                )
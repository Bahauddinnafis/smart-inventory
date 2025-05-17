# -*- coding: utf-8 -*-
{
    'name': "Smart Inventory Tracker",

    'summary': "Manajemen Stok untuk Supply Chain",

    'description': """
Proyek ini bertujuan untuk mengembangkan sistem manajemen stok yang efisien dan efektif untuk supply chain. Sistem ini akan membantu perusahaan dalam mengelola persediaan barang, memantau pergerakan barang, dan meningkatkan efisiensi operasional.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/stock_history_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'supply_chain/static/img/*',
        ],
    },
    
    # only loaded in demonstration mode
    'demo': [
        'demo/product_demo.xml',
    ],
}


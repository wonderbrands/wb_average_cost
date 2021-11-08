# -*- coding: utf-8 -*-
{
    'name': "Average Cost",

    'summary': """
        Añade el campo "Costo Promedio" en la vista de lista para el reporte de inventario""",

    'description': """
        Campo añadido al reporte de inventario que muestra el costo promedio de cada producto en el reporte de inventario
    """,

    'author': "Wonder Brands",
    'website': "https://wonderbrands.co/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '12.0.1',
    'depends': [
        'stock',
        'current_average_cost',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        #'views/product_template_views.xml',
        'views/stock_quant_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': False,
    'installable': True,
}
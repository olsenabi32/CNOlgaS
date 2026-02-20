{
    'name': 'CestaNavidadOlga',
    'summary': 'Gestión de cestas de Navidad, productos y preparación',
    'version': '19.0.1.0.0',
    'depends': ['base', 'web'],
    'author': 'Olga',
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': -10,
    'category': 'Custom',
    'description': (
        'Módulo de ejemplo para gestionar cestas de Navidad en Odoo 19.\n'
        'Incluye pantallas de Productos, Cestas y Líneas de cesta.'
    ),
    'data': [
        'security/ir.model.access.csv',
        'views/cesta_navidad_producto_views.xml',
        'views/cesta_navidad_cesta_views.xml',
        'views/cesta_navidad_linea_views.xml',
        'views/cesta_navidad_menus.xml',
    ],
}

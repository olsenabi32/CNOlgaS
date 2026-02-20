{
    'name': "agencia",
    'version': '1.0',
    'depends': ['base','web'],
    'author': "ELM",
    'application': True,
    'installable': True,
    'auto-install': False,
    'sequence': -10,
    'description': "Ejemplo creación de aplicación odoo para la clase de gestión empresarial",
    'data': [
        'security/ir.model.access.csv',
        'views/agencia_destinos_views.xml',
        'views/agencia_viajes_views.xml',
        'views/agencia_menus.xml',
    ],
    'category': 'ClaseSGERM',

}
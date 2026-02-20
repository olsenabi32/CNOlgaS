from odoo import fields, models


class CestaNavidadProducto(models.Model):
    _name = 'cestanavidadolga.producto'
    _description = 'CestaNavidadOlga_Producto'

    name = fields.Char(string='Producto', required=True)
    categoria = fields.Selection(
        [
            ('dulce', 'Dulce'),
            ('embutido', 'Embutido'),
            ('bebida', 'Bebida'),
            ('otros', 'Otros'),
        ],
        string='Categoría',
        default='otros',
        required=True,
    )
    precio = fields.Float(string='Precio unitario', required=True)
    stock = fields.Integer(string='Stock disponible', default=0, required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('check_precio_no_negativo', 'CHECK(precio >= 0)', 'El precio no puede ser negativo.'),
        ('check_stock_no_negativo', 'CHECK(stock >= 0)', 'El stock no puede ser negativo.'),
    ]

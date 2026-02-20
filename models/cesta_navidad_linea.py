from odoo import api, fields, models


class CestaNavidadLinea(models.Model):
    _name = 'cestanavidadolga.linea'
    _description = 'CestaNavidadOlga_Linea'

    cesta_id = fields.Many2one('cestanavidadolga.cesta', string='Cesta', required=True, ondelete='cascade')
    producto_id = fields.Many2one('cestanavidadolga.producto', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad', default=1, required=True)
    precio_unitario = fields.Float(string='Precio unitario', related='producto_id.precio', store=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.cantidad * line.precio_unitario

    _sql_constraints = [
        ('check_cantidad_positiva', 'CHECK(cantidad > 0)', 'La cantidad debe ser mayor que cero.'),
    ]

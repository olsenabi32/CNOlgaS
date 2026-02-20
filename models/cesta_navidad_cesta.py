from odoo import api, fields, models


class CestaNavidadCesta(models.Model):
    _name = 'cestanavidadolga.cesta'
    _description = 'CestaNavidadOlga_Cesta'

    name = fields.Char(string='Referencia', required=True)
    cliente = fields.Char(string='Cliente', required=True)
    fecha_entrega = fields.Date(string='Fecha de entrega')
    estado = fields.Selection(
        [
            ('borrador', 'Borrador'),
            ('preparacion', 'En preparación'),
            ('enviada', 'Enviada'),
            ('entregada', 'Entregada'),
        ],
        string='Estado',
        default='borrador',
        required=True,
    )
    linea_ids = fields.One2many('cestanavidadolga.linea', 'cesta_id', string='Líneas de la cesta')
    total = fields.Float(string='Total', compute='_compute_total', store=True)
    active = fields.Boolean(default=True)

    @api.depends('linea_ids.subtotal')
    def _compute_total(self):
        for record in self:
            record.total = sum(record.linea_ids.mapped('subtotal'))

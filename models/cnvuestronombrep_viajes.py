from odoo import fields, models


class CNVuestroNombrePViajes(models.Model):
    _name = 'cnvuestronombrep.viaje'
    _description = 'CNVuestroNombreP_Viaje'

    name = fields.Char(string='Nombre del viaje', required=True)
    duracion = fields.Integer(string='Días', required=True)
    fecha_inicio = fields.Date(string='Fecha de inicio')
    situacion = fields.Selection(
        [
            ('abierto', 'Abierto'),
            ('realizado', 'Realizado'),
            ('terminado', 'Terminado'),
        ],
        string='Situación',
        default='abierto',
        required=True,
    )
    destino_ids = fields.Many2many(
        'cnvuestronombrep.destino',
        'cnvuestronombrep_viaje_destino_rel',
        'viaje_id',
        'destino_id',
        string='Escalas (Destinos)',
        required=True,
    )
    active = fields.Boolean(default=True)

    _sql_constraints = [
        (
            'check_duracion_no_negativa',
            'CHECK(duracion >= 0)',
            'La duración no puede ser negativa.',
        )
    ]

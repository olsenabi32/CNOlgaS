from odoo import fields, models


class agencia_viajes(models.Model):
    _name = "agencia.viajes"
    _description = "Agencia de viajes organizados"

    name = fields.Char(string='Nombre del viaje', required=True)

    duracion = fields.Integer(string='Días', required=True)
    fec_comienzo = fields.Date(string='Fecha de inicio')
    situacion = fields.Selection([
        ('A', 'Abierto'),
        ('R', 'Realizado'),
        ('T', 'Terminado')
    ],string = 'situacion', default='A', required=True)
    escala = fields.Many2many(
        'agencia.destinos',
        string='Escala',
        required=True)
    active = fields.Boolean(default=True)
    _sql_constraints = [
        ('check_duracion', 'CHECK(duracion>=0)', 'La duracion no puede ser negativa.')
    ]

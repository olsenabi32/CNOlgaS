from odoo import fields, models


class CNVuestroNombrePDestinos(models.Model):
    _name = 'cnvuestronombrep.destino'
    _description = 'CNVuestroNombreP_Destino'

    name = fields.Char(string='Localidad', required=True)
    codigo_postal = fields.Char(string='Código Postal', size=5, required=True)
    active = fields.Boolean(default=True)
    viaje_ids = fields.Many2many(
        'cnvuestronombrep.viaje',
        'cnvuestronombrep_viaje_destino_rel',
        'destino_id',
        'viaje_id',
        string='Viajes',
    )

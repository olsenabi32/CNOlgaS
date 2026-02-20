# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ejemplo_destinos(models.Model):
    _name = "agencia.destinos"
    _description = "Destinos de los viajes programados"

    name = fields.Char(string = 'Localidad',size=50, required=True)
    codigo = fields.Char(string = 'Codigo Postal de la localidad',size = 5,required=True)
    active = fields.Boolean(default=True)
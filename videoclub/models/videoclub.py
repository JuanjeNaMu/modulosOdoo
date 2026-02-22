# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Pelicula(models.Model):
    _name = 'videoclub.pelicula'
    _description = 'Película'

    name = fields.Char(string='Título', required=True)
    director = fields.Char(string='Director')
    anio = fields.Integer(string='Año')
    genero = fields.Selection([
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
    ], string='Género', required=True)
    duracion = fields.Integer(string='Duración (minutos)')
    disponible = fields.Boolean(string='Disponible', default=True)
    caratula = fields.Binary(string='Carátula')
    
    # Campo calculado
    duracion_horas = fields.Float(string='Duración (horas)', compute='_compute_duracion_horas')
    
    @api.depends('duracion')
    def _compute_duracion_horas(self):
        for record in self:
            record.duracion_horas = record.duracion / 60.0 if record.duracion else 0.0
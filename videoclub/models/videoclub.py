# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class VideoclubPelicula(models.Model):
    _name = 'videoclub.pelicula'
    _description = 'Películas de Videoclub'
    _rec_name = 'titulo'  # Campo que se mostrará en referencias
    _order = 'titulo asc'  # Orden alfabético por título

    # Campos básicos
    titulo = fields.Char(
        string='Título',
        required=True,
        help='Título de la película',
        index=True
    )
    
    director = fields.Char(
        string='Director',
        required=True,
        help='Nombre del director'
    )
    
    anyo = fields.Integer(
        string='Año',
        required=True,
        help='Año de estreno'
    )
    
    genero = fields.Selection([
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('animacion', 'Animación'),
    ], string='Género', required=True)
    
    duracion = fields.Integer(
        string='Duración (minutos)',
        help='Duración en minutos'
    )
    
    sinopsis = fields.Text(
        string='Sinopsis',
        help='Resumen de la película'
    )
    
    disponible = fields.Boolean(
        string='Disponible',
        default=True,
        help='¿Está disponible para alquilar?'
    )
    
    caratula = fields.Binary(
        string='Carátula',
        help='Imagen de la carátula'
    )
    
    precio = fields.Float(
        string='Precio alquiler',
        digits=(6, 2),  # 6 dígitos totales, 2 decimales
        default=3.50,
        help='Precio de alquiler por día'
    )

    # Campo calculado
    duracion_horas = fields.Float(
        string='Duración (horas)',
        compute='_compute_duracion_horas',
        store=True,
        help='Duración en horas (calculado automáticamente)'
    )
    
    @api.depends('duracion')
    def _compute_duracion_horas(self):
        """Calcula la duración en horas a partir de los minutos"""
        for record in self:
            record.duracion_horas = record.duracion / 60.0 if record.duracion else 0.0
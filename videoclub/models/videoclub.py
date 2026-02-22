from odoo import models, fields

class VideoclubPelicula(models.Model):
    _name = 'videoclub.pelicula'
    _description = 'Película'

    name = fields.Char(string='Título', required=True)
    director = fields.Char(string='Director')
    anio = fields.Integer(string='Año')

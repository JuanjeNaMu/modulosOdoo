# # -*- coding: utf-8 -*-
# from odoo import models, fields, api

# class videoclub_pelis(models.Model):
#     # atributos
#     _name = 'videoclub.pelis'
#     _description = 'Película'

#     # campos
#     titulo = fields.Char('Titulo', size=30, required=True, help='Nombre de la peli')
#     director = fields.Char('Director', size=30, required=False, help='Director de la peli', default='')
#     clasificacion = fields.Selection([
#         ('TP', 'Todos los Públicos'),
#         ('men12', 'Menores de 12 años'),
#         ('may18', 'Mayores 18 años')
#     ], string='Clasificación', default='TP')
#     presupuesto = fields.Integer()
#     fechaestreno = fields.Date()

# from odoo import models, fields, api

# class videoclub_pelis(models.Model):
#     _name = 'videoclub.pelis' # Nombre técnico de la tabla [cite: 83]
#     _description = 'Película'

#     titulo = fields.Char('Titulo', size=30, required=True) [cite: 85]
#     director = fields.Char('Director', default='') [cite: 85]
#     clasificacion = fields.Selection([
#         ('TP','Todos los Públicos'),
#         ('men12','Menores de 12 años'),
#         ('may18','Mayores 18 años')
#     ], string='Clasificación', default='TP') [cite: 85]
#     presupuesto = fields.Integer() [cite: 85]
#     fechaestreno = fields.Date() [cite: 85]

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class videoclub_pelis(models.Model):
    # atributos
    _name = 'videoclub.pelis'
    _description = 'Película'

    # campos
    titulo = fields.Char('Titulo', size=30, required=True, help='Nombre de la peli')
    director = fields.Char('Director', size=30, required=False, help='Director de la peli', default='')
    clasificacion = fields.Selection([
        ('TP', 'Todos los Públicos'),
        ('men12', 'Menores de 12 años'),
        ('may18', 'Mayores 18 años')
    ], string='Clasificación', default='TP')
    presupuesto = fields.Integer()
    fechaestreno = fields.Date()
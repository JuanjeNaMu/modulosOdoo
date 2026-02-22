from odoo import models, fields

class GradingService(models.Model):
    _name = 'grading.service'
    _description = 'Servicio de Grading'

    name = fields.Char(string='Nombre', required=True)
    price = fields.Float(string='Precio', required=True)
    description = fields.Text(string='Descripción')
    request_ids = fields.One2many('grading.request', 'service_id', string='Solicitudes')

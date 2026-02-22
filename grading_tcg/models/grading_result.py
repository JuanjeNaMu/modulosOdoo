from odoo import models, fields

class GradingResult(models.Model):
    _name = 'grading.result'
    _description = 'Resultado de Grading'

    request_id = fields.Many2one('grading.request', string='Solicitud', required=True, ondelete='cascade')
    card_name = fields.Char(string='Nombre de la carta', required=True)
    grade = fields.Selection([
        ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'),
        ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')
    ], string='Puntuación', required=True)
    notes = fields.Text(string='Observaciones')

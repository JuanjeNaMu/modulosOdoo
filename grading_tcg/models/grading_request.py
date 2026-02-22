from odoo import models, fields, api
from datetime import date

class GradingRequest(models.Model):
    _name = 'grading.request'
    _description = 'Solicitud de Grading'
    _inherit = ['mail.thread']
    _order = 'id desc'

    name = fields.Char(string='Referencia', required=True, default='Nueva', copy=False)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    service_id = fields.Many2one('grading.service', string='Servicio', required=True)
    date_requested = fields.Date(string='Fecha solicitud', default=fields.Date.today, required=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('received', 'Recibido'),
        ('in_progress', 'En progreso'),
        ('done', 'Completado'),
        ('cancelled', 'Cancelado')
    ], string='Estado', default='draft', tracking=True)
    card_image = fields.Binary(string='Imagen de la carta', attachment=True)
    days_elapsed = fields.Integer(string='Días transcurridos', compute='_compute_days_elapsed', store=True)

    @api.depends('date_requested', 'state')
    def _compute_days_elapsed(self):
        for record in self:
            if record.date_requested and record.state != 'done' and record.state != 'cancelled':
                delta = date.today() - record.date_requested
                record.days_elapsed = delta.days
            else:
                record.days_elapsed = 0

    result_ids = fields.One2many('grading.result', 'request_id', string='Resultados')
    notes = fields.Text(string='Notas internas')

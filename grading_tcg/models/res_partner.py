from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    grading_request_ids = fields.One2many('grading.request', 'partner_id', string='Solicitudes de Grading')

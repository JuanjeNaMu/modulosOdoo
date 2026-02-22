# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MiModuloJuanje(models.Model):
    _name = 'mi_modulo_juanje.modelo_principal'
    _description = 'Mi Módulo Juanje'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    value = fields.Integer(string='Value')
    value2 = fields.Float(compute="_value_pc", store=True, string='Calculated Value')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
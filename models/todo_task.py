# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoTask(models.Model):
    _inherit = 'todo.task'
    user_id = field_name = fields.Many2many('res.users', 'Responsable')
    date_deadline = field_name = fields.Date('Deadline')


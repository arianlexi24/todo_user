# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoTask(models.Model):
    _inherit = 'todo.task'
    user_id = fields.Many2one('res.users', 'Responsable')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="Qu'est-ce qu'on devra faire?")


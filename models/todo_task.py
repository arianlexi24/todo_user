# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']
    user_id = fields.Many2one('res.users', 'Responsable')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="Qu'est-ce qu'on devra faire?")

    @api.multi
    def do_toggle_done(self):
        for task in self:
            if task.user_id != self.env.user:
                raise ValidationError(
                    'Seul le responsable a le droit de faire cela!')
        return super(TodoTask, self).do_toggle_done()

    @api.model
    def do_clear_done(self):
        domain = [
            ('is_done', '=', True), '|', ('user_id', '=', self.env.uid), 
            ('user_id', '=', False)
            ]
        dones = self.search(domain)
        dones.write({'active': False})
        return True 


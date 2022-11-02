# -*- coding: utf-8 -*-

from random import randint

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    def _get_default_color(self):
        return randint(1, 11)

    color = fields.Integer(string='Color', default=_get_default_color)

# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    # Set the default salesperson when a contact is created
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    # Provide multiple users access to each contact
    related_user_ids = fields.Many2many('res.users', string='Access Rights', default=lambda self: self.env.user)

    # Automatically sync salesperson and related users from parent to child
    @api.model
    def _commercial_fields(self):
        return super(ResPartner, self)._commercial_fields() + \
               ['user_id', 'related_user_ids']

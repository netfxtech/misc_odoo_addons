# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    # Tag a company_id if filtering by company_id is too restrictive or need to filter multiple companies in a report
    related_company_ids = fields.Many2many('res.company', string='Primary Company',
                                           default=lambda self: self.env.company)

    # Automatically sync salesperson and related users from parent to child
    @api.model
    def _commercial_fields(self):
        return super(ResPartner, self)._commercial_fields() + \
               ['related_company_ids']

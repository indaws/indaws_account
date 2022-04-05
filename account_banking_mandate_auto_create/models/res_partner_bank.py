# -*- coding: utf-8 -*-
from odoo import models, api, fields


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    @api.model_create_multi
    def create(self, vals):
        bank_line = super(ResPartnerBank, self).create(vals)
        self.env['account.banking.mandate'].create({
            'format': 'sepa',
            'type': 'recurrent',
            'scheme': 'CORE',
            'recurrent_sequence_type': 'recurring',
            'signature_date': fields.Date.today(),
            'state': 'valid',
            'partner_bank_id': bank_line.id,
            'partner_id': bank_line.partner_id.id
        })
        return bank_line

# -*- encoding: utf-8 -*-
#
#    Module Writen to OpenERP, Open Source Management Solution
#    Coded by: Alan Guzman(jage2201@gmail.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from odoo import models, fields, api


class WizardReportInvoicesState(models.TransientModel):
    _name = 'wizard.report.invoices.state'

    invoice_state = fields.Selection(
    [
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('paid', 'Paid'),
        ('cancel', 'Cancel'),
        ('all', 'All'),
        ], 'Invoice state',
        required=True)

    @api.multi
    def generate_report(self):
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'module_pch.report_state_invoices',
            'context': self.env.context,
        }

    @api.multi
    def get_invoices(self):
        invoice_obj = self.env['account.invoice']
        if self.invoice_state == 'draft':
            invoice_ids = invoice_obj.search(
                [('type', '=', 'out_invoice'),
                 ('state', '=', 'draft')])
        elif self.invoice_state == 'open':
            invoice_ids = invoice_obj.search(
                [('type', '=', 'out_invoice'),
                 ('state', '=', 'open')])
        elif self.invoice_state == 'paid':
            invoice_ids = invoice_obj.search(
                [('type', '=', 'out_invoice'),
                 ('state', '=', 'paid')])
        elif self.invoice_state == 'cancel':
            invoice_ids = invoice_obj.search(
                [('type', '=', 'out_invoice'),
                 ('state', '=', 'cancel')])
        elif self.invoice_state == 'all':
            invoice_ids = invoice_obj.search(
                [('type', '=', 'out_invoice')])
        return invoice_ids

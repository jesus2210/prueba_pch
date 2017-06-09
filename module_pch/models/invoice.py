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
from odoo import models, fields, api, _
from odoo.exceptions import except_orm


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    boss_validate = fields.Boolean('Validate for boss', readonly=True)

    @api.multi
    def validate_boss(self):
        for invoice in self:
            invoice.boss_validate = True


    @api.multi
    def invoice_validate(self):
        for inv in self:
            if inv.boss_validate:
                return super(AccountInvoice, self).invoice_validate()
            else:
                raise except_orm(
                    _('Warning!'), _(
                        'Chief approval required to validate invoice'))

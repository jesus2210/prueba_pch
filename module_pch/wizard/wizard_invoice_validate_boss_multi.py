# coding: utf-8
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Coded by: Alan Guzmán(jage2201@gmail.com)
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
from odoo import models, api


class ValidateBossInvoiceMulti(models.TransientModel):
    _name = 'wizard.boss.validate.invoice.multi'

    @api.multi
    def validate_boss_invoice_multi(self):
        if self.env.context.get('active_model', '') == 'account.invoice':
            ids = self.env.context.get('active_ids', [])
            inv_obj = self.env['account.invoice']
            inv_obj.browse(ids).validate_boss()

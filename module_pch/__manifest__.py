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
{
    "name": "Extra validation for invoices",
    "version": "1.0",
    "category": "Accounting",
    "description": """
    This module adds extra validations when validating invoices and \
    generates a pdf report
    """,
    "license": "AGPL-3",
    "depends": [
     'account',
    ],
    "demo": [],
    "data": [
        'views/invoice_view.xml'
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
    "active": False
}

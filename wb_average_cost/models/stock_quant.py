# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, tools, SUPERUSER_ID
from io import StringIO, BytesIO
from odoo.tools.translate import _
from odoo.tools import email_re, email_split
from odoo.exceptions import UserError, AccessError

_logger = logging.getLogger(__name__)

class StockQuant(models.Model):
    _inherit = "stock.quant"

    average = fields.Char(string='Costo Promedio',compute='_relation', track_visibility='onchange')

    @api.depends('product_id')
    def _relation(self):
        self.ensure_one()

        self.average = self.product_id.avarage_cost
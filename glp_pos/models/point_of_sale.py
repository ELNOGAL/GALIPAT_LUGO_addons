# -*- coding: utf-8 -*-
# © 2019 Pedro Gómez <pegomez@elnogal.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import tools
from openerp import models, fields


class PosSession(models.Model):
    _inherit = "pos.session"

    product_summary_ids = fields.One2many('product.summary.session', 'session_id', 'Product Summary', readonly=True)


class ProductSummarySession(models.Model):
    _name = "product.summary.session"
    _description = "Group products on pos sessions"
    _auto = False
    _rec_name = 'product_id'
    _order = 'product_id'

    session_id = fields.Many2one('pos.session', 'Pos Session', readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    qty = fields.Float('Quantity', readonly=True)
    price_unit = fields.Float('Price unit', readonly=True)
    price_subtotal = fields.Float('Subtotal', readonly=True)
    price_subtotal_incl = fields.Float('Total', readonly=True)

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        cr.execute(
            """CREATE or REPLACE VIEW %s as (
            SELECT
                row_number() over()          AS id,
                ps.id                        AS session_id,
                pol.product_id               AS product_id,
                SUM(pol.qty)                 AS qty,
                pol.price_unit               AS price_unit,
                SUM(pol.price_subtotal)      AS price_subtotal,
                SUM(pol.price_subtotal_incl) AS price_subtotal_incl
            FROM pos_order_line pol
            JOIN pos_order po ON po.id = pol.order_id
            JOIN pos_session ps ON ps.id = po.session_id
            GROUP BY ps.id,
                     pol.product_id,
                     pol.price_unit
            ORDER BY ps.id,
                     pol.product_id
            )"""
            % (self._table)
        )

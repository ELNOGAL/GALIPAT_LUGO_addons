# -*- coding: utf-8 -*-
# © 2019 Pedro Gómez <pegomez@elnogal.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "GALIPAT POS",
    'version': '8.0.0.0.0',
    'author': 'Pedro Gómez <pegomez@elnogal.com>',
    'category': 'Custom',
    'license': 'AGPL-3',
    'description': """Módulo que contiene customizaciones para Galipat relacionadas con POS""",
    'depends': [
        'base',
        'point_of_sale'
    ],
    'contributors': [
        "Pedro Gómez <pegomez@elnogal.com>"
    ],
    'data': [
        'views/report_sessionsummary_custom.xml',
        'views/point_of_sale_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True
}

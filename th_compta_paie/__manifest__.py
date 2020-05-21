# -*- coding: utf-8 -*-
{
    'name' : 'Comptabilité de paie',
    'version' : '3.0.0',
    'summary' : """
        Module ajoutant la comptabilité de paie à Odoo paie
    """,
    'category' : 'Tools',
    'author' : 'Thomas ATCHA',
    'maintainer' : 'Thomas ATCHA',
    'company': 'Thomas ATCHA',
    'website' : 'https://www.roots.ws',
    'depends' : ['base','hr','hr_payroll','account'],
    'data' : [
        'security/ir.model.access.csv',
        'compta_view.xml',
    ],

    'images' : [],
    'licence' : 'AGPL-5',
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
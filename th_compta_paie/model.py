# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ComptaPayeRule(models.Model):
	_inherit = 'hr.salary.rule'

	compte_debit_id = fields.Many2one(
	    'account.account',
	    string='Compte de débit',
	 )
	compte_credit_id = fields.Many2one(
	    'account.account',
	    string='Compte de crédit',
	)
	@api.onchange('compte_debit_id')
	def _onchange_compte_debit_id(self):
	    for rec in self:
	    	rec.compte_credit_id = rec.compte_debit_id



class ComptaPayeRuleCategory(models.Model):
	_inherit = 'hr.salary.rule.category'

	compte_debit_id = fields.Many2one(
	    'account.account',
	    string='Compte de débit',
	 )
	compte_credit_id = fields.Many2one(
	    'account.account',
	    string='Compte de crédit',
	)

	@api.onchange('compte_debit_id')
	def _onchange_compte_debit_id(self):
	    for rec in self:
	    	rec.compte_credit_id = rec.compte_debit_id
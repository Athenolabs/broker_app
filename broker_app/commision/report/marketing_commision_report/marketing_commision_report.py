# Copyright (c) 2013, bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["No Marketing:Link/Marketing:200","Nama:Data:200","Komisi:Currency:200","Pph:Currency:200","Komisi bersih:Currency:200"], []
	branch=""
	if filters.get("branch"):
		branch = """ and dk.branch = "{}" """.format(filters.get("branch"))
	data = frappe.db.sql("""select 
		cmd.marketing, cmd.nama, sum(cmd.commision_value),sum(cmd.pph),sum(cmd.net_commision) 
		from `tabCommision Marketing Detail` cmd 
		join `tabData Komisi` dk on cmd.parent=dk.name where dk.date between "{}" and "{}" {} group by marketing""".format(filters.get("from"),filters.get("to"),branch),as_list=1)
	return columns, data

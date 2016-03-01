
# Copyright (c) 2013, bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	branch=""
	if filters.get("branch"):
		branch = """ and dk.branch= "{}" """.format(filters.get("branch"))
	data=frappe.db.sql("""select cmd.marketing,m.nama,sum(point) 
		from `tabPV` cmd 
		left join `tabData Komisi` dk on cmd.parent=dk.name 
		left join `tabMarketing` m on cmd.marketing=m.name 
		where cmd.docstatus=1 and cmd.posting_date between "{}" and "{}" {} group by cmd.marketing""".format(filters.get("from"),filters.get("to"),branch))
	columns=["No Marketing:Marketing/Link:200","Nama:Data:200","Total:Currency:200"]
	return columns, data

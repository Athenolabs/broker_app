# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PV(Document):
	def on_submit(self):
		data = frappe.db.sql("""select sum(point) from tabPV where marketing="{}" and docstatus<=1 """.format(self.marketing),as_list=1)
		total=0
		for x in data:
			total = total+x[0]
		#total = get_total_pv(self.marketing)
		data = frappe.db.sql("""select commision from `tabJenjang Karir` where terget<={}  order by commision asc""".format(total),as_list=1)
		jk=50
		for x in data:
			if x[0]>jk:
				jk = x[0]
		#jk = get_jk(total)
		data = frappe.db.get("Marketing",{"name":self.marketing})
		if jk>data.commision:
			frappe.db.sql("""update tabMarketing set commision={} where name="{}" """.format(jk,self.marketing))
	def get_total_pv(marketing):
		data = frappe.db.sql("""select sum(point) from tabPV where marketing="{}" and docstatus=1 """.format(marketing),as_list=1)
		total=0
		for x in data:
			total = total+x[0]
		return total
	def get_jk(total):
		data = frappe.db.sql("""select commision from `tabJenjang Karir` where terget=<{} and docstatus=1 order by commision asc LIMIT 0,1""".format(total),as_list=1)
		result=50
		for x in data:
			result = x[0]
		return result


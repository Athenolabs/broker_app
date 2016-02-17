# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DataKomisi(Document):
	def validate(self):
		listing_count=0
		selling_count=0
		koor_count=0
		for marketing in self.commision_list:
			if marketing.type == "Listing":
				listing_count=listing_count+1
			elif marketing.type == "Selling":
				selling_count=selling_count+1
			elif marketing.type == "Koordinator":
				koor_count=koor_count+1
		if listing_count>2 or selling_count>2 or koor_count>2:
			frappe.throw("Maximum 2 marketing untuk Selling / Listing / Koordinator")

	def on_submit(self):
		pass

	def get_marketing_list(self):
		if self.data_transaksi:
			data = frappe.db.sql("""select marketing,nama,kantor,type from `tabTransaction Marketing Detail` where parent="{}" """.format(self.data_transaksi),as_list=1)
			for row in data:
				dt = self.append('commision_list', {})
				dt.marketing=row[0]
				dt.nama=row[1]
				dt.kantor=row[2]
				dt.type=row[3]

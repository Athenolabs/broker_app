# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DataTransaksi(Document):
	def validate(self):
		listing_count=0
		selling_count=0
		for marketing in self.marketing_list:
			if marketing.type == "Listing":
				listing_count=listing_count+1
			elif marketing.type == "Selling":
				selling_count=selling_count+1
		if listing_count>1 or selling_count>2:
			frappe.throw("Maximum 2 marketing untuk Selling dan 1 untuk Listing")

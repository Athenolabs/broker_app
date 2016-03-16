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
		total_komisi=0
		if self.is_co and self.is_co==1:
			total_komisi=self.commision_co
		for marketing in self.commision_list:
			if marketing.type == "Listing" :
				listing_count=listing_count+1
				total_komisi=total_komisi+marketing.bruto
			elif marketing.type == "Selling":
				selling_count=selling_count+1
				total_komisi=total_komisi+marketing.bruto
			elif marketing.type == "Koordinator":
				koor_count=koor_count+1
				total_komisi=total_komisi+marketing.bruto
		if listing_count>1 or selling_count>2 or koor_count>2:
			frappe.throw("Maximum 2 marketing untuk Selling / 1 untuk Listing / 2 untuk Koordinator")
		if total_komisi>100:
			frappe.throw("Maximum Komisi adalah 100%")
		for marketing in self.commision_list:
			if marketing.type == "Listing" :
				marketing.tut=0
			elif marketing.type == "Selling":
				marketing.tut=1/selling_count
			elif marketing.type == "Koordinator":
				marketing.tut=0

	def on_submit(self):
		for marketing in self.commision_list:
			if marketing.pv>0:
				record = frappe.get_doc({
			 		"doctype":"PV",
			 		"marketing":marketing.marketing,
			 		"point":marketing.pv,
			 		"data_komisi":self.name,
			 		"idx":marketing.name,
			 		"posting_date":self.date
				})
				record.insert()
				record.submit()
			if marketing.tut>0:
				record = frappe.get_doc({
			 		"doctype":"TUT",
			 		"marketing":marketing.marketing,
			 		"point":marketing.tut,
			 		"data_komisi":self.name,
			 		"idx":marketing.name,
			 		"posting_date":self.date
				})
				record.insert()
				record.submit()

	def get_marketing_list(self):
		if self.data_transaksi:
			data = frappe.db.sql("""select md.marketing,md.nama,md.kantor,md.type,m.commision from `tabTransaction Marketing Detail` md join tabMarketing m on md.marketing=m.name where md.parent="{}" """.format(self.data_transaksi),as_list=1)
			self.commision_list=[]
			for row in data:
				dt = self.append('commision_list', {})
				dt.marketing=row[0]
				dt.nama=row[1]
				dt.kantor=row[2]
				dt.type=row[3]
				dt.commision=row[4]
			if self.primary_project !="" and self.type=="Jual Primary":
				primary=frappe.db.get("Primary Project",{"name":self.primary_project})
				if primary.Koordinator and primary.Koordinator!="":
					koordinator = frappe.db.get("Marketing",{"name":primary.koordinator})
					dt = self.append('commision_list', {})
					dt.marketing=primary.koordinator
					dt.nama=koordinator.nama
					dt.kantor=koordinator.kantor
					dt.type="Koordinator"
					dt.commision=primary.koor_commision
				if primary.Listing and primary.Listing!="":
					listing = frappe.db.get("Marketing",{"name":primary.listing})
					dt = self.append('commision_list', {})
					dt.marketing=primary.listing
					dt.nama=listing.nama
					dt.kantor=listing.kantor
					dt.type="Koordinator"
					dt.commision=primary.listing_commision
	def on_cancel(self):
		frappe.db.sql("""update tabPV set docstatus=2 where data_komisi="{}" """.format(self.name),as_list=1)
		frappe.db.sql("""update tabTUT set docstatus=2 where data_komisi="{}" """.format(self.name),as_list=1)
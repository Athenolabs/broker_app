# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import throw,_,msgprint
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
				if self.type=="Jual Primary":
					marketing.tut=0
				else:
					marketing.tut=1/listing_count
					#msgprint("tes {} = 1 / {}".format(marketing.tut,listing_count))
			elif marketing.type == "Selling":
				marketing.tut=1/selling_count
			elif marketing.type == "Koordinator":
				marketing.tut=0
		find=frappe.db.sql("""select count(1),name from `tabData Komisi` where docstatus<2 and data_transaksi='{}'""".format(self.data_transaksi),as_list=1)
		for row in find:
			if row[0]==0:
				frappe.throw("Transaksi sudah di gunakan pada document komisi {}".format(row[1]))
		
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
			if self.primary_project  and self.type=="Jual Primary":
				primary=frappe.db.get("Primary Project",{"name":self.primary_project})
				#frappe.msgprint(primary)
				if primary.koordinator:
					#frappe.msgprint("here")
					koordinator = frappe.db.get("Marketing",{"name":primary.koordinator})
					dt2 = self.append('commision_list', {})
					dt2.marketing=primary.koordinator
					dt2.nama=koordinator.nama
					dt2.kantor=koordinator.branch
					dt2.type="Koordinator"
					dt2.commision=primary.koor_commision
				if primary.listing :
					listing = frappe.db.get("Marketing",{"name":primary.listing})
					dt3 = self.append('commision_list', {})
					dt3.marketing=primary.listing
					dt3.nama=listing.nama
					dt3.kantor=listing.branch
					dt3.type="Listing"
					dt3.commision=primary.listing_commision
	def on_cancel(self):
		frappe.db.sql("""update tabPV set docstatus=2 where data_komisi="{}" """.format(self.name),as_list=1)
		frappe.db.sql("""update tabTUT set docstatus=2 where data_komisi="{}" """.format(self.name),as_list=1)
def available_transaction(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select dt.name,dt.alamat from `tabData Transaksi` dt 
		left join `tabData Komisi` dk on dk.data_transaksi=dt.name and dk.docstatus<2
		where dk.name is NULL and dt.docstatus=1 and (dt.name like %(txt)s
				or dt.alamat like %(txt)s)
		limit %(start)s, %(page_len)s""".format(**{
			'key': searchfield
		}), {
			'txt': "%%%s%%" % txt,
			'_txt': txt.replace("%", ""),
			'start': start,
			'page_len': page_len
		})

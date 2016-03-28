# Copyright (c) 2013, bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Keterangan:Data:400","Bruto:Currency:200","PPH:Currency:200","Komisi:Currency:200","PV:Currency:200"], []
	data.append(["<strong>{} - {}</strong>".format(filters.get("marketing"),frappe.db.get_value("Marketing",filters.get("marketing"), "nama")),"","","",""])
	data.append(["<strong>{} - {}</strong>".format(filters.get("from"),filters.get("to")),"","","",""])
	data.append(["<strong>Data Transaksi Secondary</strong>","","","",""])
	second = frappe.db.sql("""select dk.alamat,cmd.commision_value,cmd.pph,cmd.net_commision,cmd.pv
		from `tabCommision Marketing Detail` cmd 
		join `tabData Komisi` dk on cmd.parent=dk.name 
		where cmd.marketing = "{}" 
		and cmd.type IN ("Listing","Selling") 
		and dk.type like "%Secondary" 
		and dk.docstatus=1 
		and dk.date between "{}" and "{}" """.format(filters.get("marketing"),filters.get("from"),filters.get("to")),as_list=1)
	bruto,pph,komisi,pv=0,0,0,0
	for row in second:
		data.append(row)
		bruto=bruto+row[1]
		pph=pph+row[2]
		komisi = komisi+row[3]
		pv=pv+row[4]
	data.append(["<strong>Total</strong>",bruto,pph,komisi,pv])
	data.append(["","","","",""])

	data.append(["<strong>Data Transaksi Primary</strong>","","","",""])
	second = frappe.db.sql("""select dk.alamat,cmd.commision_value,cmd.pph,cmd.net_commision,cmd.pv
		from `tabCommision Marketing Detail` cmd 
		join `tabData Komisi` dk on cmd.parent=dk.name 
		where cmd.marketing = "{}" and cmd.type IN ("Listing","Selling") and dk.docstatus=1 and dk.type like "%Primary" and dk.date between "{}" and "{}" """.format(filters.get("marketing"),filters.get("from"),filters.get("to")),as_list=1)
	bruto2,pph2,komisi2,pv2=0,0,0,0
	for row in second:
		data.append(row)
		bruto2=bruto2+row[1]
		pph2=pph2+row[2]
		komisi2 = komisi2+row[3]
		pv2=pv2+row[4]
	data.append(["<strong>Total</strong>",bruto2,pph2,komisi2,pv2])
	data.append(["","","","",""])

	data.append(["<strong>Data Transaksi Koordinator</strong>","","","",""])
	second = frappe.db.sql("""select dk.alamat,cmd.commision_value,cmd.pph,cmd.net_commision,cmd.pv
		from `tabCommision Marketing Detail` cmd 
		join `tabData Komisi` dk on cmd.parent=dk.name 
		where cmd.marketing = "{}" and cmd.type NOT IN ("Listing","Selling") and dk.docstatus=1 and dk.type like "%Primary" and dk.date between "{}" and "{}" """.format(filters.get("marketing"),filters.get("from"),filters.get("to")),as_list=1)
	bruto3,pph3,komisi3,pv3=0,0,0,0
	for row in second:
		data.append(row)
		bruto3=bruto3+row[1]
		pph3=pph3+row[2]
		komisi3 = komisi3+row[3]
		pv3=pv3+row[4]
	data.append(["<strong>Total</strong>",bruto3,pph3,komisi3,pv3])
	data.append(["","","","",""])

	data.append(["<strong>Rekapitulasi Total</strong>","","","",""])
	data.append(["<strong>Transaksi Secondary</strong>",bruto,pph,komisi,pv])
	data.append(["<strong>Transaksi Primary</strong>",bruto2,pph2,komisi2,pv2])
	data.append(["<strong>Transaksi Koordinator</strong>",bruto3,pph3,komisi3,pv3])
	data.append(["<strong>Total</strong>",bruto+bruto2+bruto3,pph+pph2+pph3,komisi+komisi2+komisi3,pv+pv2+pv3])
	return columns, data

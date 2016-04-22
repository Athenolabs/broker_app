# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import cstr, now_datetime, cint, flt
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

	def on_cancel(self):
		for row in self.deadline:
			opts={
				"owner": row.name,
				"starts_on": row.tanggal,
				"subject": ('Follow up Deadline ' + self.name),
				"description": row.note
			}
			self.delete_events()

	def on_submit(self):
		for row in self.deadline:
			opts={
				"owner": row.name,
				"starts_on": row.tanggal,
				"subject": ('Follow up Deadline ' + cstr(self.name)),
				"description": row.note
			}	
			self._add_calendar_event(opts)

	def delete_events(self):
		events = frappe.db.sql_list("""select name from `tabEvent`
			where ref_type=%s and ref_name=%s""", (self.doctype, self.name))
		if events:
			frappe.db.sql("delete from `tabEvent` where name in (%s)"
				.format(", ".join(['%s']*len(events))), tuple(events))

			frappe.db.sql("delete from `tabEvent Role` where parent in (%s)"
				.format(", ".join(['%s']*len(events))), tuple(events))

	def _add_calendar_event(self, opts):
		opts = frappe._dict(opts)

		event = frappe.get_doc({
			"doctype": "Event",
			"owner": opts.owner or self.owner,
			"subject": opts.subject,
			"description": opts.description,
			"starts_on":  opts.starts_on,
			"event_type": "Private",
			"ref_type": self.doctype,
			"ref_name": self.name
		})

		event.insert(ignore_permissions=True)


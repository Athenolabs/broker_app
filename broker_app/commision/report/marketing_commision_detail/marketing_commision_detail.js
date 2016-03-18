// Copyright (c) 2016, bobby and contributors
// For license information, please see license.txt

frappe.query_reports["Marketing Commision Detail"] = {
	"filters": [
		{
			"fieldname":"from",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd":1
		},
		{
			"fieldname":"to",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": get_today(),
			"reqd":1
		},
		{
			"fieldname":"marketing",
			"label": __("Marketing"),
			"fieldtype": "Link",
			"options": "Marketing",
			"reqd":1
		}
	],
	"formatter": function(row, cell, value, columnDef, dataContext, default_formatter) {
		//value = default_formatter(row, cell, value, columnDef, dataContext);

		if (value[1]=="" or value[0]=="Total") {
			var $value = $(value).css("font-weight", "bold");
		}

		return value;
	}
}

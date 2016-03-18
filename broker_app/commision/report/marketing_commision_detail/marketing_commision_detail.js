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
		if (columnDef.df.fieldname=="Keterangan") {
			if (dataContext[columnDef.df.fieldname]=="Total"){
				value = $(value).css("font-weight", "bold");	
			}
			
		}

		return value;
	}
}

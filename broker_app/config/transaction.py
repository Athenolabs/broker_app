from frappe import _

def get_data():
	return [
		{
			"label": _("Master Data"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Marketing",
					"label":"Data Marketing"
				},
				{
					"type": "doctype",
					"name": "Primary Project",
					"label":"Data Primary Project"
				}
			]
		},
		{
			"label": _("Transaksi"),
			"icon": "icon-list",
			"items": [
				{
					"type": "doctype",
					"name": "Data Transaksi"
				},
			
			]
		}
	]

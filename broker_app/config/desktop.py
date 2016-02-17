# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Sales",
			"color": "grey",
			"icon": "octicon octicon-organization",
			"type": "module",
			"label": _("Sales")
		},                {
                        "module_name": "Administration",
                        "color": "grey",
                        "icon": "octicon octicon-pencil",
                        "type": "module",
                        "label": _("Administration")
                },                {
                        "module_name": "Commision",
                        "color": "grey",
                        "icon": "octicon octicon-law",
                        "type": "module",
                        "label": _("Commision")
                }
	]

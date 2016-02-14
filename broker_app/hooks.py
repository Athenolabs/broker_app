# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "broker_app"
app_title = "Broker App"
app_publisher = "bobby"
app_description = "-"
app_icon = "octicon octicon-organization"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/broker_app/css/broker_app.css"
# app_include_js = "/assets/broker_app/js/broker_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/broker_app/css/broker_app.css"
# web_include_js = "/assets/broker_app/js/broker_app.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "broker_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "broker_app.install.before_install"
# after_install = "broker_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "broker_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"broker_app.tasks.all"
# 	],
# 	"daily": [
# 		"broker_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"broker_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"broker_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"broker_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "broker_app.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "broker_app.event.get_events"
# }


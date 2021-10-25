# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "kautenburger_it"
app_title = "Kautenburger IT"
app_publisher = "Kautenburger IT"
app_description = "Anpassungen für Kautenburger IT"
app_icon = "octicon octicon-file-directory"
app_color = "#49B95C"
app_email = "contact@kautenburger-it.de"
app_license = "GPLv3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = ["/assets/kautenburger_it/css/task.css"]
# app_include_js = "/assets/kautenburger_it/js/kautenburger_it.js"

# include js, css files in header of web template
# web_include_css = "/assets/kautenburger_it/css/kautenburger_it.css"
# web_include_js = "/assets/kautenburger_it/js/kautenburger_it.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "kautenburger_it.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "kautenburger_it.install.before_install"
# after_install = "kautenburger_it.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kautenburger_it.notifications.get_notification_config"

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
# 		"kautenburger_it.tasks.all"
# 	],
# 	"daily": [
# 		"kautenburger_it.tasks.daily"
# 	],
# 	"hourly": [
# 		"kautenburger_it.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kautenburger_it.tasks.weekly"
# 	]
# 	"monthly": [
# 		"kautenburger_it.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "kautenburger_it.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kautenburger_it.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "kautenburger_it.task.get_dashboard_data"
# }


app_name = "custom_layer"
app_title = "custom_layer"
app_publisher = "joshua"
app_description = "just a custom layer"
app_email = "joshua@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "custom_layer",
# 		"logo": "/assets/custom_layer/logo.png",
# 		"title": "custom_layer",
# 		"route": "/custom_layer",
# 		"has_permission": "custom_layer.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom_layer/css/custom_layer.css"
app_include_js = "/assets/custom_layer/js/custom_layer.js"

# include js, css files in header of web template
# web_include_css = "/assets/custom_layer/css/custom_layer.css"
web_include_js = "/assets/custom_layer/js/custom_layer.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "custom_layer/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "custom_layer/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "custom_layer.utils.jinja_methods",
# 	"filters": "custom_layer.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "custom_layer.install.before_install"
after_install = "custom_layer.setup.set_default_logos"

# Login CAPTCHA
# -------------
before_login = ["custom_layer.recaptcha.before_login"]

# after_migrate
# -------------
after_migrate = "custom_layer.setup.set_default_logos"

# Branding
# --------
# Blank the app name ("ERPNext") shown as the sidebar subtitle.
extend_bootinfo = ["custom_layer.branding.extend_bootinfo"]

# Uninstallation
# ------------

# before_uninstall = "custom_layer.uninstall.before_uninstall"
# after_uninstall = "custom_layer.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "custom_layer.utils.before_app_install"
# after_app_install = "custom_layer.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "custom_layer.utils.before_app_uninstall"
# after_app_uninstall = "custom_layer.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "custom_layer.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_layer.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["custom_layer.search.awesomebar_results"]

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"custom_layer.tasks.all"
# 	],
# 	"daily": [
# 		"custom_layer.tasks.daily"
# 	],
# 	"hourly": [
# 		"custom_layer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"custom_layer.tasks.weekly"
# 	],
# 	"monthly": [
# 		"custom_layer.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "custom_layer.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "custom_layer.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "custom_layer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "custom_layer.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["custom_layer.utils.before_request"]
# after_request = ["custom_layer.utils.after_request"]

# Job Events
# ----------
# before_job = ["custom_layer.utils.before_job"]
# after_job = ["custom_layer.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"custom_layer.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


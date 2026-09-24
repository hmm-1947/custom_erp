import frappe


def extend_bootinfo(bootinfo):
	"""Hide the app name ("ERPNext") that Frappe shows as the sidebar
	subtitle under the workspace title.

	The sidebar reads `frappe.boot.app_data[*].app_title`, which comes
	from each app's `app_title` hook. We blank it here (per request) so
	the text never reaches the browser, rather than hiding it with CSS.
	Runs after Frappe builds bootinfo.app_data, via `extend_bootinfo`.
	"""
	for app in bootinfo.get("app_data") or []:
		app["app_title"] = ""

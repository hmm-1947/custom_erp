import frappe

DEFAULT_LOGO = "/assets/custom_layer/images/logo-dark.png"
FAVICON = "/assets/custom_layer/images/favicon.png"


def set_default_logos():
	"""Point the server-rendered logo fields at our own branding so the
	default Frappe logo never flashes before custom_layer.js can swap it
	for dark-theme users. Safe to run repeatedly (idempotent)."""
	navbar_settings = frappe.get_single("Navbar Settings")
	if navbar_settings.app_logo != DEFAULT_LOGO:
		navbar_settings.app_logo = DEFAULT_LOGO
		navbar_settings.save(ignore_permissions=True)

	website_settings = frappe.get_single("Website Settings")
	changed = False
	if website_settings.app_logo != DEFAULT_LOGO:
		website_settings.app_logo = DEFAULT_LOGO
		changed = True
	if website_settings.splash_image != DEFAULT_LOGO:
		website_settings.splash_image = DEFAULT_LOGO
		changed = True
	# Browser-tab icon. Website Settings.favicon overrides ERPNext's default
	# favicon for both the login/website pages and the desk.
	if website_settings.favicon != FAVICON:
		website_settings.favicon = FAVICON
		changed = True
	# Hide the "Powered by ERPNext" web footer. footer_info.html only falls
	# back to ERPNext's template when this field is falsy, and the value is
	# ignored when empty, so use a single non-breaking space (invisible).
	if website_settings.footer_powered != "&nbsp;":
		website_settings.footer_powered = "&nbsp;"
		changed = True
	if changed:
		website_settings.save(ignore_permissions=True)

	# Drop the standard "Sent via ERPNext" line from outgoing emails.
	# (Custom email-account footers are unaffected.)
	system_settings = frappe.get_single("System Settings")
	if not system_settings.disable_standard_email_footer:
		system_settings.disable_standard_email_footer = 1
		system_settings.save(ignore_permissions=True)

	frappe.db.commit()

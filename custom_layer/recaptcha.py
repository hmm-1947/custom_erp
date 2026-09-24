import frappe
from frappe import _


RECAPTCHA_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"


@frappe.whitelist(allow_guest=True, methods=["GET"])
def get_site_key():
	"""Public endpoint so the login page JS can render the widget.
	Returns an empty string if reCAPTCHA isn't configured on this site.
	"""
	return frappe.conf.get("recaptcha_site_key") or ""


def before_login(login_manager=None):
	"""Hooked via `before_login` in hooks.py. Verifies the Google
	reCAPTCHA v2 token submitted with the login form before any
	credential check runs. Raises frappe.AuthenticationError on
	failure, which aborts the login attempt.
	"""
	secret_key = frappe.conf.get("recaptcha_secret_key")
	if not secret_key:
		# Not configured on this site; skip silently rather than
		# locking everyone out of login.
		return

	token = frappe.form_dict.get("g-recaptcha-response") or frappe.form_dict.get("recaptcha_response")

	if not token:
		frappe.throw(_("Please complete the CAPTCHA to continue."), frappe.AuthenticationError)

	try:
		import requests

		response = requests.post(
			RECAPTCHA_VERIFY_URL,
			data={
				"secret": secret_key,
				"response": token,
				"remoteip": frappe.local.request_ip,
			},
			timeout=5,
		)
		result = response.json()
	except Exception:
		frappe.log_error(title="reCAPTCHA verification request failed")
		frappe.throw(_("Could not verify CAPTCHA. Please try again."), frappe.AuthenticationError)

	if not result.get("success"):
		frappe.throw(_("CAPTCHA verification failed. Please try again."), frappe.AuthenticationError)

import frappe


def execute():
    navbar_settings = frappe.get_single("Navbar Settings")

    for item in navbar_settings.help_dropdown:
        if item.item_label in {"About", "Frappe Support"}:
            item.hidden = 1

    navbar_settings.save(ignore_permissions=True)

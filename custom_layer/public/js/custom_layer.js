frappe.provide("custom_layer");

(function () {
    const original_create_menu = frappe.ui.create_menu;

    frappe.ui.create_menu = function (opts) {
        if (opts.parent && opts.parent[0]?.classList.contains("desktop-avatar") && Array.isArray(opts.menu_items)) {
            opts = {
                ...opts,
                menu_items: opts.menu_items.filter(
                    (item) => !["About", "Frappe Support"].includes(item.label)
                ),
            };
        }

        return original_create_menu.call(this, opts);
    };
})();
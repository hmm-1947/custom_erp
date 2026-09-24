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

// Theme-aware home/sidebar/splash logo.
// Light theme uses logo-dark.png; dark theme uses logo.png.
// Navbar Settings > App Logo and Website Settings > Splash Image are set to
// logo-dark.png as the server-rendered default (see
// custom_layer.setup.set_default_logos), so light-theme users see the
// correct logo immediately with no flash. This script swaps it for
// dark-theme users and keeps things in sync on live theme toggles.
(function () {
    const lightLogo = "/assets/custom_layer/images/logo-dark.png";
    const darkLogo = "/assets/custom_layer/images/logo.png";

    function updateHomeLogo() {
        const theme = document.documentElement.getAttribute("data-theme");
        const logo = theme === "dark" ? darkLogo : lightLogo;
        const logoUrl = new URL(logo, window.location.origin).href;

        document.querySelectorAll(".navbar-brand .app-logo, #brand-logo, .splash img").forEach((img) => {
            if (img.tagName === "IMG" && img.src !== logoUrl) {
                img.src = logo;
            }
        });

        // NOTE: the desk sidebar header (.sidebar-header .header-logo) is
        // intentionally NOT touched. Frappe fills it with the icon of the
        // module/workspace the user opened (Projects, Buying, ...), and that
        // per-module icon must be left alone.
    }

    // Login / update-password page logo: always logo-dark.png (server
    // default already matches this; JS here is just a safety net).
    function updateLoginLogo() {
        const loginLogoUrl = new URL(lightLogo, window.location.origin).href;

        document.querySelectorAll(".page-card-head .app-logo").forEach((img) => {
            if (img.src !== loginLogoUrl) {
                img.src = lightLogo;
            }
        });
    }

    const observer = new MutationObserver((mutations) => {
        if (mutations.some((mutation) =>
            mutation.type === "attributes" ||
            mutation.addedNodes.length
        )) {
            updateHomeLogo();
            updateLoginLogo();
        }
    });

    function init() {
        updateHomeLogo();
        updateLoginLogo();

        observer.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ["data-theme"],
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true,
        });
    }

    if (document.body) {
        init();
    } else {
        document.addEventListener("DOMContentLoaded", init, { once: true });
    }
})();

// Google reCAPTCHA v2 (checkbox) on the login page.
// Renders the widget under the password field of the main sign-in form
// only, disables the submit button until it's solved, and attaches the
// token to the login request (window.login.call). The token is single
// use, so the widget is reset after every login attempt.
(function () {
    let widgetId = null;
    let token = "";

    function loadRecaptchaScript(cb) {
        if (window.grecaptcha && window.grecaptcha.render) return cb();
        window.__custom_layer_recaptcha_onload = cb;
        const script = document.createElement("script");
        script.src = "https://www.google.com/recaptcha/api.js?onload=__custom_layer_recaptcha_onload&render=explicit";
        script.async = true;
        script.defer = true;
        document.head.appendChild(script);
    }

    function setSubmitDisabled(disabled) {
        document.querySelectorAll(".for-login .btn-login").forEach((btn) => {
            btn.disabled = disabled;
        });
    }

    function resetWidget() {
        token = "";
        if (widgetId !== null && window.grecaptcha) {
            window.grecaptcha.reset(widgetId);
        }
        setSubmitDisabled(true);
    }

    function renderWidget(container, siteKey) {
        if (container.dataset.recaptchaRendered) return;
        container.dataset.recaptchaRendered = "1";

        const holder = document.createElement("div");
        holder.className = "custom-layer-recaptcha";
        holder.style.margin = "12px 0";
        container.appendChild(holder);

        widgetId = window.grecaptcha.render(holder, {
            sitekey: siteKey,
            callback: (t) => {
                token = t;
                setSubmitDisabled(false);
            },
            "expired-callback": () => {
                token = "";
                setSubmitDisabled(true);
            },
            "error-callback": () => {
                // Never lock users out if Google's widget itself errors
                // (e.g. network blocked or misconfigured key).
                token = "";
                setSubmitDisabled(false);
            },
        });

        setSubmitDisabled(true);
    }

    function init() {
        // The login form can be served at /login or at / (when a guest
        // hits the site root), so detect it by the DOM, not the URL.
        if (!document.querySelector(".for-login .page-card-body")) return;

        fetch("/api/method/custom_layer.recaptcha.get_site_key")
            .then((r) => r.json())
            .then((data) => {
                const siteKey = data.message;
                if (!siteKey) return; // not configured; don't block login

                loadRecaptchaScript(() => {
                    // Only the main sign-in form needs the CAPTCHA.
                    const container = document.querySelector(".for-login .page-card-body");
                    if (container) renderWidget(container, siteKey);
                });
            })
            .catch(() => {
                // If the check itself fails, don't lock users out of login.
            });
    }

    function patchLoginCall() {
        if (!window.login || window.login.__recaptcha_patched) return false;

        const original = window.login.call;
        window.login.call = function (args, callback, url) {
            const isLogin = url === "/api/method/login";
            if (isLogin && token) {
                args["g-recaptcha-response"] = token;
            }
            const result = original.call(this, args, callback, url);
            if (isLogin && result && typeof result.always === "function") {
                // Tokens are single-use: reset after every attempt so a
                // failed login can be retried.
                result.always(resetWidget);
            }
            return result;
        };
        window.login.__recaptcha_patched = true;
        return true;
    }

    function waitForLogin() {
        if (patchLoginCall()) return;
        const interval = setInterval(() => {
            if (patchLoginCall()) clearInterval(interval);
        }, 100);
    }

    if (document.body) {
        init();
        waitForLogin();
    } else {
        document.addEventListener("DOMContentLoaded", () => {
            init();
            waitForLogin();
        }, { once: true });
    }
})();

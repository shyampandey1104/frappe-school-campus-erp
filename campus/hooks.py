# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "campus"
app_title = "Frappe School Campus Erp"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe School Campus Erp - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/campus/css/campus.bundle.css"
app_include_js = "/assets/campus/js/campus.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe School Campus Erp Entry": {
        "validate": "campus.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "campus.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "campus.tasks.hourly_sync"
    ],
    "daily": [
        "campus.tasks.daily_reconciliation"
    ],
    "weekly": [
        "campus.tasks.weekly_digest"
    ]
}

# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "campus"
app_title = "Frappe School Campus Erp"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe School Campus Erp for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/campus/css/campus.bundle.css"
app_include_js = "/assets/campus/js/campus.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "campus.engine.on_document_submit",
        "on_cancel": "campus.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "campus.engine.daily_scheduled_sync"
    ]
}

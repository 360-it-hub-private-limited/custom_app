// Copyright (c) 2024, pankaj@360ithub.com and contributors
// For license information, please see license.txt

frappe.query_reports["Developer wise Contribution in Projects"] = {
	"filters": [
        {
            "fieldname": "employee",
            "label": __("Employee"),
            "fieldtype": "Link",
            "options": "Employee",
            "reqd": 1,  // This makes the filter mandatory
            "default": "" // Optionally set a default value if needed
        }
	]
};

import frappe

def get_context(context):
    if not frappe.session.user:
        frappe.local.flags.redirect_location = "/login"
        raise frappe.Redirect

    # Get the session user
    session_user = frappe.session.user

    # Fetch all records from the "Issue" doctype where the "user" field is equal to the session user
    issues = frappe.get_list("S Issue", filters={"user": session_user}, fields=["name","project_name", "subject", "status"])

    # Add the fetched issues to the context
    context.issues = issues

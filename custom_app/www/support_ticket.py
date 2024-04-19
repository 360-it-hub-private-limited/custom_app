# Your Frappe module (e.g., apps/custom_app/custom_app/www/support_ticket.py)

import frappe

def get_context(context):
    if not frappe.session.user:
        frappe.local.flags.redirect_location = "/login"  # Replace "/login" with the actual URL of your login page
        raise frappe.Redirect

    # Get the session user
    session_user = frappe.session.user

    # Find the user in the "S Project" DocType based on customer_mail_id
    s_project = frappe.get_list(
        "S Project",
        filters={"customer_mail_id": session_user},
        fields=["name", "customer", "customer_mail_id"]
    )

    # Check if a matching record is found
    if s_project:
        project_name = s_project[0].name
        customer = s_project[0].customer
        customer_mail_id = s_project[0].customer_mail_id
    else:
        project_name = None
        customer = None
        customer_mail_id = None

    # Fetch the list of projects dynamically from the database
    projects, common_customer, common_customer_mail_id = get_projects_list(session_user)

    context.update({
        "project_name": project_name,
        "customer": customer,
        "customer_mail_id": customer_mail_id,
        "projects": projects,
        "common_customer": common_customer,  # Add common_customer to the context
        "common_customer_mail_id": common_customer_mail_id  # Add common_customer_mail_id to the context
    })

    # Add other context variables or processing as needed
    # ...

def get_projects_list(session_user):
    # Fetch the list of projects from the "S Project" DocType based on customer_mail_id
    projects = frappe.get_all("S Project", filters={"customer_mail_id": session_user}, fields=["name", "project_name", "customer", "customer_mail_id"])

    # Check if any projects are found
    if projects:
        # Extract the common customer and customer_mail_id from the first project (assuming all projects have the same customer and customer_mail_id)
        common_customer = projects[0].customer
        common_customer_mail_id = projects[0].customer_mail_id
    else:
        common_customer = None
        common_customer_mail_id = None

    # Create a list of dictionaries with "value" and "label" keys
    projects_list = [{"value": project.name, "label": project.project_name, "customer": project.customer, "customer_mail_id": project.customer_mail_id} for project in projects]

    return projects_list, common_customer, common_customer_mail_id




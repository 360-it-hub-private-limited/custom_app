import frappe

def get_context(context):
    # Get the session user
    session_user = frappe.session.user

    # Add the session user to the context dictionary
    context.user = session_user

    # Example: You can also set a default value for the User field
    context.default_user = session_user

    # Find the project associated with the session user
    project = frappe.get_all("S Project", filters={"customer_mail_id": session_user}, fields=["name", "customer_mail_id","customer"])
	# frappe.mgsprint(project)
    if project:
		# context.customer = project.customer
        # Get the customer_mail_id from the project
        context.project_name =", ".join([i.get("name") for i in project])
        context.customer_name =", ".join([i.get("customer") for i in project])
		# print()
    else:
        # Set a default value if the project is not found
        context.project_name = None
        context.customer_name = None

    # You can do more with the context as needed
    # ...

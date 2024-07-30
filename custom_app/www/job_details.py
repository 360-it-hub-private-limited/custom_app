import frappe
from frappe import _

def get_context(context):
    # Get the ID from the URL
    job_opening_id = frappe.form_dict.get('id')

    # Example: Retrieve job opening details by ID
    if job_opening_id:
        job_opening = frappe.get_doc("Job Opening", job_opening_id)

        # Now you can access the properties of the job_opening document
        context.designation = job_opening.get("designation")
        context.job_title = job_opening.get("job_title")
        context.description = job_opening.get("description")
        context.location = job_opening.get("location")
        context.posting_date = job_opening.get("posted_on")
        context.job_type = job_opening.get("job_type")
        context.closes_on = job_opening.get("closes_on")
        context.vacancy = job_opening.get("vacancy")
        context.name = job_opening.get("name")

        # You can add more properties as needed
        # context.some_other_property = job_opening.get("some_other_property")

import frappe
from frappe import _

def get_context(context):
    job_opening = frappe.get_list("Job Opening",
        filters={"status": "open"},
        fields=["job_title", "designation", "location","posted_on","name"],
    )
    
    # Get the count of job openings
    job_opening_count = len(job_opening)

    # Add job opening list and count to the context
    context.job_opening = job_opening
    context.job_opening_count = job_opening_count

	

	# teams = frappe.get_list("Buloke Team",
							
    #                     filters={"is_published":1},
	# 	                fields=["name1","image","role"],)

	# context.teams = teams
	


	# gallery = frappe.get_list("Buloke Gallery",
	# 	filters={"is_published":1},
	# 	fields=["image","is_published"],
	# )

	# context.gallery = gallery
import frappe
from frappe import _

def get_context(context):
    blog = frappe.get_list("Blogs",
        filters={"is_published": 1},
        fields=["blog_image", "blog_heading", "blog_content","posted_on","name"],
    )
    
    # Get the count of job openings
    blog_count = len(blog)

    # Add job opening list and count to the context
    context.blog = blog
    context.blog_count = blog_count

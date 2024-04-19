import frappe
from frappe import _

def get_context(context):
    # Get the ID from the URL
    blog_details_id = frappe.form_dict.get('id')

    # Example: Retrieve job opening details by ID
    if blog_details_id:
        blog_details = frappe.get_doc("Blogs", blog_details_id)

        # Now you can access the properties of the blog_details document
        context.blog_image = blog_details.get("blog_image")
        context.name = blog_details.get("name")
        context.blog_heading = blog_details.get("blog_heading")
        context.posted_on = blog_details.get("posted_on")
        context.blog_content = blog_details.get("blog_content")
        context.publisher_name = blog_details.get("publisher_name")
        # context.posting_date = blog_details.get("posted_on")
        # context.job_type = blog_details.get("job_type")
        # context.closes_on = blog_details.get("closes_on")
        # context.vacancy = blog_details.get("vacancy")
        # context.name = blog_details.get("name")

        # You can add more properties as needed
        # context.some_other_property = blog_details.get("some_other_property")
        comments = frappe.get_all("Blog Comment", filters={"blog_id": blog_details_id}, fields=["name", "comment","commented_on_date"])
        context.comment_len = len(comments)
        # Pass comments to context
        context.comments = comments



# @frappe.whitelist(allow_guest=True)
# def submit_comment():
#     comment_text = frappe.form_dict.get('comment_text')
#     blog_post_id = frappe.form_dict.get('blog_post_id')  # Make sure to pass the blog post ID
    
#     # Save the comment
#     comment = frappe.new_doc("Comment")
#     comment.comment_text = comment_text
#     comment.parent = blog_post_id
#     comment.insert()

#     # You can add additional logic if needed

#     return "Comment submitted successfully"
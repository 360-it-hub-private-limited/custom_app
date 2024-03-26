from frappe import _
import frappe
import urllib.parse

@frappe.whitelist(allow_guest=True)
def process_form_data(form_data):

    try:
        
        name = frappe.form_dict.get("name")
        email = frappe.form_dict.get("email")
        phone_no = frappe.form_dict.get("phone")
        subject = frappe.form_dict.get("subject")
        message = frappe.form_dict.get("message")
        # erp_development = frappe.form_dict.get("erp_development")
        # mobile_application_development = frappe.form_dict.get("mobile_application_development")
        # custom_website_development = frappe.form_dict.get("custom_website_development")
        # e_commerce_solution = frappe.form_dict.get("e_commerce_solution")
        # uiux_solutions = frappe.form_dict.get("uiux_solutions")

        # Debugging: Print the values to check if they are correct
        # frappe.msgprint("field1 ==> " + str(name1) + " and field2 = " + str(email))
        # pass
        # frappe.msgprint(form_data)
        parsed_data = urllib.parse.parse_qs(form_data)
        # frappe.msgprint(parsed_data)

        # Extract values
        # csrf_token = parsed_data.get("csrf_token", [None])[0]
        name = parsed_data.get("name", [None])[0]
        email = parsed_data.get("email", [None])[0]
        phone_no = parsed_data.get("phone", [None])[0]
        subject = parsed_data.get("subject", [None])[0]
        message = parsed_data.get("message", [None])[0]
        # Adjust checkbox values to be 1 for selected, and 0 for unselected
        erp_development = "1" if parsed_data.get("erp_development") else "0"
        mobile_application_development = "1" if parsed_data.get("mobile_application_development") else "0"
        custom_website_development = "1" if parsed_data.get("custom_website_development") else "0"
        e_commerce_solution = "1" if parsed_data.get("e_commerce_solution") else "0"
        uiux_solutions = "1" if parsed_data.get("uiux_solutions") else "0"

        # Create a dictionary of selected checkboxes
        selected_checkboxes = {
            "erp_development": erp_development,
            "mobile_application_development": mobile_application_development,
            "custom_website_development": custom_website_development,
            "e_commerce_solution": e_commerce_solution,
            "uiux_solutions": uiux_solutions,
        }


        # frappe.msgprint("Form data ==> "+form_data)
        
        # field1_value = frappe.form_dict.get("field1")
        # field2_value = frappe.form_dict.get("field2")
        # field3_value = frappe.form_dict.get("csrf_token")
        # frappe.msgprint(field1)

        # Replace "YourCustomDoctype" with the actual name of your Doctype
        custom_data_doc = frappe.new_doc("Contact Form")
        custom_data_doc.name1 = name
        custom_data_doc.email = email
        custom_data_doc.phone_no = phone_no
        custom_data_doc.subject = subject
        custom_data_doc.message = message
        custom_data_doc.erp_development = erp_development
        custom_data_doc.mobile_application_development = mobile_application_development
        custom_data_doc.custom_website_development = custom_website_development
        custom_data_doc.e_commerce_solutions = e_commerce_solution
        custom_data_doc.uiux_solutions = uiux_solutions
        # frappe.msgprint("Form data ==> "+custom_data_doc)

        # Save the document to persist the changes
        custom_data_doc.insert()

        return ("Data inserted successfully.")
    except Exception as e:
        frappe.log_error(str(e))
        return "Error inserting data: " + str(e)



@frappe.whitelist(allow_guest=True)
def process_form_data_blog(form_data):

    try:
        
        name = frappe.form_dict.get("name")
        comment_text = frappe.form_dict.get("comment_text")
      
        parsed_data = urllib.parse.parse_qs(form_data)
       
        name = parsed_data.get("name", [None])[0]
        comment_text = parsed_data.get("comment_text", [None])[0]
        


    

        # Replace "YourCustomDoctype" with the actual name of your Doctype
        blog = frappe.new_doc("Blog Comment")
        blog.blog_id = name
        blog.comment = comment_text
        
        # frappe.msgprint("Form data ==> "+blog)

        # Save the document to persist the changes
        blog.insert()

        return ("Data inserted successfully.")
    except Exception as e:
        frappe.log_error(str(e))
        return "Error inserting data: " + str(e)


# from frappe.utils.file_manager import save_file


# @frappe.whitelist(allow_guest=True)
# def jobapply(form_data):

#     try:
#         title = frappe.form_dict.get("title")
#         name = frappe.form_dict.get("name")
#         email = frappe.form_dict.get("email")
#         phone_no = frappe.form_dict.get("phone")
#         resume = frappe.form_dict.get("resume")
#         cover_letter = frappe.form_dict.get("cover_letter")

#         # Debugging: Print the values to check if they are correct
#         # frappe.msgprint("field1 ==> " + str(name1) + " and field2 = " + str(email))
#         # pass
#         # frappe.msgprint(form_data)
#         parsed_data = urllib.parse.parse_qs(form_data)
#         # frappe.msgprint(parsed_data)

#         # Extract values
#         # csrf_token = parsed_data.get("csrf_token", [None])[0]
#         title = parsed_data.get("title", [None])[0]
#         name = parsed_data.get("name", [None])[0]
#         email = parsed_data.get("email", [None])[0]
#         phone_no = parsed_data.get("phone", [None])[0]
#         resume = parsed_data.get("resume", [None])[0]
#         cover_letter = parsed_data.get("cover_letter", [None])[0]

#         # frappe.msgprint("field1 ==> "+name1+" and field2 = "+ email + phone_no+requirement)
#         # pass


#         # frappe.msgprint("Form data ==> "+form_data)
        
#         # field1_value = frappe.form_dict.get("field1")
#         # field2_value = frappe.form_dict.get("field2")
#         # field3_value = frappe.form_dict.get("csrf_token")
#         # frappe.msgprint(field1)

#         # Replace "YourCustomDoctype" with the actual name of your Doctype
#         custom_data_doc = frappe.new_doc("Job Applicant")
#         custom_data_doc.job_title = title
#         custom_data_doc.applicant_name = name
#         custom_data_doc.email_id = email
#         custom_data_doc.phone_number = phone_no
#         custom_data_doc.cover_letter = cover_letter
#         # custom_data_doc.resume_attachment = resume
#         # custom_data_doc.cover_letter = cover_letter
#         # frappe.msgprint("Form data ==> "+custom_data_doc)

#         # Save the document to persist the changes
#         custom_data_doc.insert()

#         # Get the saved document
#         # ticket = frappe.get_doc("Job Applicant", ticket.name)

        
#         # Check if resume file is attached in the form data
#         if "resume" in frappe.request.files:
#             uploaded_file = frappe.request.files.get("resume")
#             resume_file = save_file(uploaded_file.name, uploaded_file.content, None, None, custom_data_doc.name,decode=True)

#             # Update the resume_attachment field with the file URL
#             custom_data_doc.resume_attachment = resume_file.file_url
#             custom_data_doc.save()

#         return "Data inserted successfully."
#     except Exception as e:
#         frappe.log_error(str(e))
#         return "Error inserting data: " + str(e)




import frappe
from frappe.utils.file_manager import save_file

@frappe.whitelist(allow_guest=True)
def jobapply(form_data=None, **kwargs):
    try:
        # Parse the form_data
        parsed_data = urllib.parse.parse_qs(form_data)

        # Retrieve values more safely using get method with default value
        title = parsed_data.get("title", [None])[0]
        name = parsed_data.get("name", [None])[0]
        email = parsed_data.get("email", [None])[0]
        phone_no = parsed_data.get("phone", [None])[0]
        cover_letter = parsed_data.get("cover_letter", [None])[0]
        resume_link = parsed_data.get("resume_url", [None])[0]

        # Check for required fields
        if name is None:
            return "Error: Applicant Name is required."

        # Check for required fields
        if email is None:
            return "Error: Email Address is required."
        # Your existing code for creating Job Applicant document
        job_applicant = frappe.new_doc("Job Applicant")
        job_applicant.job_title = title
        job_applicant.applicant_name = name
        job_applicant.email_id = email
        job_applicant.phone_number = phone_no
        job_applicant.cover_letter = cover_letter
        job_applicant.resume_link = resume_link
        job_applicant.insert()


        # if 'file' not in frappe.request.files:
        #     return frappe.throw("No file attached to the request")

        # uploaded_file = frappe.request.files['file']
        
        # # Save the file using Frappe's save_file function
        # file_doc = save_file(uploaded_file.name, uploaded_file.content)
        if "resume" in frappe.request.files:
            uploaded_file = frappe.request.files.get("resume")

            # Save the file
            file_doc = save_file(
                file_name=uploaded_file.name,
                content=uploaded_file.content,
                is_private=0,  # Set to 1 if the file should be private
                folder=job_applicant.get("folder"),  # Set the target folder
            )

            # Attach the file to the job applicant document
            job_applicant.resume_attachment = file_doc.file_url
            job_applicant.save()

            return "Data inserted successfully with file upload."

        return "Data inserted successfully without file upload."

    except Exception as e:
        frappe.log_error("Error inserting data: " + str(e))
        return "Error inserting data. Please try again. Error: " + str(e)




import frappe
from frappe.utils.file_manager import save_file

@frappe.whitelist(allow_guest=True)
def support_ticket(form_data=None, **kwargs):
    try:
        # Parse the form_data
        parsed_data = urllib.parse.parse_qs(form_data)

        # Retrieve values more safely using get method with default value
        email = parsed_data.get("email", [None])[0]
        customername = parsed_data.get("customername", [None])[0]
        project = parsed_data.get("project", [None])[0]
        subject = parsed_data.get("subject", [None])[0]
        description = parsed_data.get("description", [None])[0]

        # Check for required fields
        if customername is None:
            return "Error: customername Address is required."

        # Your existing code for creating S Issue document
        s_issue = frappe.new_doc("S Issue")
        s_issue.subject = subject
        s_issue.project = project
        s_issue.customer = customername
        s_issue.user = email
        s_issue.description = description
        s_issue.created_on_website = 1
        s_issue.insert()

        # Return only the ID of the created S Issue document
        return s_issue.name

    except Exception as e:
        frappe.log_error("Error inserting data: " + str(e))
        return "Error inserting data. Please try again. Error: " + str(e)







@frappe.whitelist(allow_guest=True)
def apply_for_job(form_data=None, **kwargs):
    try:
        # Parse the form_data
        parsed_data = urllib.parse.parse_qs(form_data)

        # Retrieve values more safely using get method with default value
        # title = parsed_data.get("title", [None])[0]
        name = parsed_data.get("name", [None])[0]
        email = parsed_data.get("email", [None])[0]
        phone_no = parsed_data.get("phone", [None])[0]
        cover_letter = parsed_data.get("cover_letter", [None])[0]
        resume_link = parsed_data.get("resume_url", [None])[0]
        job_role = parsed_data.get("role", [None])[0]

        # Check for required fields
        if name is None:
            return "Error: Applicant Name is required."

        # Check for required fields
        if email is None:
            return "Error: Email Address is required."
        # Your existing code for creating Job Applicant document
        apply_for_job = frappe.new_doc("Apply For Job")
        # apply_for_job.job_title = title
        apply_for_job.name1 = name
        apply_for_job.email = email
        apply_for_job.mobile_no = phone_no
        apply_for_job.description = cover_letter
        apply_for_job.resume_url = resume_link
        apply_for_job.job_role = job_role
        apply_for_job.insert()


        # if 'file' not in frappe.request.files:
        #     return frappe.throw("No file attached to the request")

        # uploaded_file = frappe.request.files['file']
        
        # # Save the file using Frappe's save_file function
        # file_doc = save_file(uploaded_file.name, uploaded_file.content)
        if "resume" in frappe.request.files:
            uploaded_file = frappe.request.files.get("resume")

            # Save the file
            file_doc = save_file(
                file_name=uploaded_file.name,
                content=uploaded_file.content,
                is_private=0,  # Set to 1 if the file should be private
                folder=job_applicant.get("folder"),  # Set the target folder
            )

            # Attach the file to the job applicant document
            job_applicant.resume_attachment = file_doc.file_url
            job_applicant.save()

            return "Data inserted successfully with file upload."

        return "Data inserted successfully without file upload."

    except Exception as e:
        frappe.log_error("Error inserting data: " + str(e))
        return "Error inserting data. Please try again. Error: " + str(e)

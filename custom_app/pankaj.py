# import frappe

# @frappe.whitelist()
# def get_tasks_for_project(project_id):
#     # Query tasks associated with the given project_id
#     tasks = frappe.get_all('S Task', filters={'project': project_id}, fields=['name', 'subject', 'progress', 'actual_time'])

#     # Calculate the total actual_time
#     total_actual_time = sum(float(task.get('actual_time', 0)) for task in tasks)

#     # Return the list of tasks and the total actual_time
#     return {'tasks': tasks, 'total_actual_time': total_actual_time}


# @frappe.whitelist()
# def share_lead_with_user(project_name, user):
#     frappe.share.add('S Project', project_name, user, read=1, write=0)
#     return "Success"
 

# @frappe.whitelist()
# def remove_share_access(project_name, user):
#     try:
#         # Your code to remove share access goes here
#         # Example:
#         frappe.share.remove('S Project', project_name, user)

#         return {"user": user, "message": "Share access removed successfully."}
#     except Exception as e:
#         frappe.log_error(_("Error removing share access for {0}").format(user), title="Remove Share Access Error")
#         frappe.throw(_("Error removing share access. Please try again."))


# @frappe.whitelist()
# def get_users_with_access(project_name):
#     try:
#         # Your code to fetch the list of users with access goes here
#         # Example:
#         users_with_access = frappe.share.get_users("S Project", project_name)

#         # Return the list of users
#         return {"users": users_with_access}
#     except Exception as e:
#         frappe.log_error("Error getting users with access for project {0}".format(project_name), title="Get Users with Access Error")
#         frappe.throw("Error getting users with access. Please try again.")




# custom_app/pankaj.py

from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist()
def get_tasks_for_project(project_id):
    try:
        # Your code to fetch tasks for the project goes here
        # Example:
        tasks = frappe.get_all("S Task", filters={"project": project_id}, fields=["name", "subject", "progress", "actual_time", "expected_time","task_status","users"])

        total_actual_time = sum([float(task.get("actual_time") or 0) for task in tasks])

        return {"tasks": tasks, "total_actual_time": total_actual_time}
    except Exception as e:
        frappe.log_error("Error fetching tasks for project {0}".format(project_id), title="Get Tasks Error")
        frappe.throw("Error fetching tasks. Please try again.")




@frappe.whitelist()
def get_shared_users(project_name):
    shared_users = frappe.get_all('DocShare', filters={'share_doctype': 'S Project', 'name': project_name})
    return [{"user": user.user} for user in shared_users]

@frappe.whitelist()
def remove_user_from_project(project_name, user):
    frappe.share.remove('S Project', project_name, user)

@frappe.whitelist()
def remove_user_from_tasks(project_name, user):
    tasks = frappe.get_all('S Task', filters={'project': project_name})
    for task in tasks:
        frappe.share.remove('S Task', task.name, user)

@frappe.whitelist()
def share_user_with_project(project_name, user):
    try:
        # Check if the project document exists
        project_exists = frappe.get_value('S Project', project_name, 'name')
        if not project_exists:
            frappe.throw("Project not found. Please check the project name.")

      
        
        # Share the project document with the specified user
        frappe.share.add('S Project', project_name, user, read=1, write=0)

        # Share associated tasks with the specified user
        tasks = frappe.get_all('S Task', filters={'project': project_name})
        for task in tasks:
            frappe.share.add('S Task', task.name, user, read=1, write=1)

        return {"user": user, "message": "Document shared successfully with {0}.".format(user)}
    except Exception as e:
        # frappe.log_error("Error sharing document with {0} for project {1}".format(user, project_name), title="Share Lead Error")
        frappe.throw("Error sharing document. Please try again. Error: {}".format(str(e)))


# @frappe.whitelist()
# def remove_user_with_project(project_name, user):
#     existing_shares = frappe.get_all('DocShare', filters={'share_doctype': 'S Project', 'share_name': project_name, 'user': ('!=', user)}, fields=['name'])
#     # print(existing_shares)
#     for share in existing_shares:
#         frappe.delete_doc('DocShare', share['name'])
    

@frappe.whitelist()
def remove_user_with_project(project_name, user):
    try:
        # Remove share access for the project document
        existing_shares_project = frappe.get_all('DocShare', filters={'share_doctype': 'S Project', 'share_name': project_name, 'user': ('!=', user)}, fields=['name'])
        for share in existing_shares_project:
            frappe.delete_doc('DocShare', share['name'])

        # Remove share access for associated tasks
        tasks = frappe.get_all('S Task', filters={'project': project_name})
        for task in tasks:
            existing_shares_task = frappe.get_all('DocShare', filters={'share_doctype': 'S Task', 'share_name': task.name, 'user': ('!=', user)}, fields=['name'])
            for share in existing_shares_task:
                frappe.delete_doc('DocShare', share['name'])

        return {"user": user, "message": "Share access removed successfully for {0}.".format(user)}
    except Exception as e:
        # frappe.log_error("Error removing share access for {0} in project {1}".format(user, project_name), title="Remove Share Access Error")
        frappe.throw("Error removing share access. Please try again. Error: {}".format(str(e)))




@frappe.whitelist()
def get_user_for_project(project_name):
    # Get the 'S Project' document
    project_doc = frappe.get_doc('S Project', project_name)

    if project_doc:
        # Access the table field 'userss'
        userss = project_doc.get('userss', [])

        # Extract user values from each row
        user_list = [row.user for row in userss]

        # Remove duplicate users, if any
        unique_users = list(set(user_list))
        
        return unique_users
    else:
        return None



# def remove_share_access_except_user(project_name, user):
#     # Fetch all shares for the specified document
#     shares = frappe.get_all('DocShare', filters={'document_type': 'S Project', 'document_name': project_name}, fields=['user'])
    
#     # Remove share access for all users except the specified user
#     for share in shares:
#         if share.user != user:
#             frappe.share.remove('S Project', project_name, share.name)

# @frappe.whitelist()
# def get_users_with_access(project_name):
#     try:
#         # Your code to fetch users with access to the project goes here
#         # Example:
#         users_with_access = frappe.share.get_users('S Project', project_name)

#         return {"users": users_with_access}
#     except Exception as e:
#         frappe.log_error("Error fetching users with access for project {0}".format(project_name), title="Get Users with Access Error")
#         frappe.throw("Error fetching users with access. Please try again.")

# @frappe.whitelist()
# def remove_share_access(project_name, user):
#     try:
#         # Fetch the document name based on the project_name
#         document_name = frappe.get_value("S Project", {"name": project_name}, "name")

#         if document_name:
#             # Fetch existing shares for the document
#             existing_shares = frappe.get_all("DocShare", filters={"share_doctype": "S Project", "share_name": document_name, "user": user})

#             # Remove existing shares for the user
#             for share in existing_shares:
#                 frappe.delete_doc("DocShare", share.name, ignore_permissions=True)

#             return {"user": user, "message": "Share access removed successfully for {0}.".format(user)}
#         else:
#             frappe.throw("Document not found for project {0}".format(project_name))

#     except Exception as e:
#         frappe.log_error("Error removing share access for {0} on project {1}".format(user, project_name), title="Remove Share Access Error")
#         frappe.throw("Error removing share access. Please try again.")


import frappe

@frappe.whitelist()
def get_s_task_list():
    # Your logic to fetch S Task records
    # For example, fetching from a Frappe doctype named 'S Task'
    s_task_list = frappe.get_all('S Task', filters={}, fields=['name', 'status'])

    return s_task_list




@frappe.whitelist()
def task_with_issue_creation(i_id):
    issue = frappe.get_last_doc("S Issue", filters={"name": i_id})

    if not issue:
        return f"Issue {i_id} not found"

    issue_task = frappe.get_all("S Task", filters={"issue": i_id})

    if issue_task:
        return f"Task already created for Issue {i_id}"

    task = frappe.get_doc({
        "doctype": "S Task",
        "subject": issue.subject,
        "custom_customer_id": issue.customer,
        "priority": issue.priority,
        "issue": issue.name,
        "project": issue.project,
        "description": issue.description,
        "modules": issue.modules,
        # "custom_task_type": issue.issue_type,
    })

    task.insert()

    print(issue.subject)

    return f"New Task created for Issue {i_id}"
    
    
    
    
    
@frappe.whitelist()
def share_user_with_customer(project_name, customer_email):
    # Validate user access or any other necessary checks

    # Assuming you have a 'Shared User' doctype to store shared users
    frappe.share.add('S Project', project_name, customer_email, read=1)

    return "Document shared with {0} for read access."
    
    
    
    
@frappe.whitelist()
def get_tasks_for_project_status(project_id):
    tasks = frappe.get_all("S Task", filters={"project": project_id}, fields=["task_status"])
    return tasks




@frappe.whitelist()
def get_task_statuses_and_priorities():
    # Fetch distinct task statuses and priorities using SQL
    sql_query = """
        SELECT DISTINCT task_status
        FROM `tabS Task`
    """
    statuses = frappe.db.sql(sql_query, as_dict=True)

    sql_query = """
        SELECT DISTINCT priority
        FROM `tabS Task`
    """
    priorities = frappe.db.sql(sql_query, as_dict=True)

    # Extract values from query results
    unique_statuses = [status['task_status'] for status in statuses]
    unique_priorities = [priority['priority'] for priority in priorities]

    return {
        'statuses': unique_statuses,
        'priorities': unique_priorities
    }



@frappe.whitelist()
def get_tasks_for_project_status_1(project_id):
    # Query to fetch tasks based on project_id
    tasks = frappe.get_list('S Task',
                            filters={'project': project_id},
                            fields=['name', 'task_status', 'priority','users'])
    tasks_unallocated = frappe.get_list('S Task',
                            filters={'project': project_id,'users':''},
                            fields=['name', 'task_status', 'priority'])
    # print ('sdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',len(tasks_unallocated))
    return tasks





import frappe

@frappe.whitelist()
def get_tasks_by_user_for_project(project_id, users):
    if not users:
        return []

    users = frappe.parse_json(users)

    # Fetch tasks for the given project and selected users
    tasks = frappe.get_all('S Task', filters={
        'project': project_id,
        'users': ['in', users]
    }, fields=['name', 'users', 'task_status', 'priority'])

    return tasks




import frappe

@frappe.whitelist()
def get_projects_for_user(session_user):
    projects = frappe.get_list(
        'S Project',
        filters={'userss': ['like', '%' + session_user + '%']},
        fields=['name']
    )
    return projects

# @frappe.whitelist()
# def get_tasks_for_project(project_name):
#     tasks = frappe.get_list(
#         'S Task',
#         filters={'project': project_name},
#         fields=['name', 'subject', 'task_status', 'priority', 'users']
#     )
#     return tasks
# In your custom app's Python file (e.g., my_custom_app/my_custom_app/doctype/s_project/s_project.py)

# In your custom app's Python file (e.g., custom_app/custom_app/pankaj.py)

import frappe
from frappe import _

@frappe.whitelist()
def get_project_users(project_name):
    try:
        # Fetch the project document
        project = frappe.get_doc('S Project', project_name)
        
        # Check if userss field exists and is not empty
        if project and project.userss:
            # Ensure userss is returned as a list
            if isinstance(project.userss, list):
                return project.userss
            else:
                return project.userss.split('\n')
        else:
            return []
    except Exception as e:
        frappe.log_error(f"Error fetching project users for {project_name}: {str(e)}")
        return []

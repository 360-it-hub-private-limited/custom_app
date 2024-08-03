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


#with out project status
# @frappe.whitelist()
# def get_projects_for_user(session_user):
#     try:
#         projects = frappe.db.sql("""
#             SELECT
#                 DISTINCT parent AS name
#             FROM
#                 `tabMultiselect User`
#             WHERE
#                 user = %s
#             AND parenttype = 'S Project'
#         """, (session_user), as_dict=True)
#         return projects
#     except Exception as e:
#         frappe.log_error(f"Error fetching projects for user: {str(e)}", "get_projects_for_user")
#         return []


# With project status
@frappe.whitelist()
def get_projects_for_user(session_user):
    try:
        projects = frappe.db.sql("""
            SELECT DISTINCT
                name
            FROM
                `tabS Project`
            WHERE
                name IN (
                    SELECT DISTINCT
                        parent
                    FROM
                        `tabMultiselect User`
                    WHERE
                        user = %s
                        AND parenttype = 'S Project'
                )
                AND status = 'Open'
        """, (session_user), as_dict=True)
        return projects
    except Exception as e:
        frappe.log_error(f"Error fetching projects for user: {str(e)}", "get_projects_for_user")
        return []


@frappe.whitelist()
def get_tasks_information(project_name,user):
    try:
        # Fetch tasks with no users assigned (unallocated time)
        unallocated_tasks = frappe.get_all(
            'S Task',
            filters={
                'project': project_name,
                'users':''
                
            },
            fields=['name', 'expected_time']
        )
        
        total_unallocated_time = sum([task.expected_time for task in unallocated_tasks if task.expected_time])
        unallocated_task_count = len(unallocated_tasks)

        # Fetch tasks assigned to the session user with status Assigned or In Development
        assigned_tasks = frappe.get_all(
            'S Task',
            filters={
                'project': project_name,
                'users': user,
                # 'task_status': ['in', ['Assigned', 'In Development','Open']]
                'task_status': ['!=', 'Completed']
            },
            fields=['name', 'expected_time']
        )

        assigned_working_hours = sum([task.expected_time for task in assigned_tasks if task.expected_time])
        assigned_task_count = len(assigned_tasks)

        total_available_working_hours = total_unallocated_time + assigned_working_hours

        return {
            "total_unallocated_time": total_unallocated_time,
            "unallocated_task_count": unallocated_task_count,
            "assigned_working_hours": assigned_working_hours,
            "assigned_task_count": assigned_task_count,
            "total_available_working_hours": total_available_working_hours
        }
    except Exception as e:
        frappe.log_error(f"Error fetching tasks information for project {project_name}: {str(e)}", "get_tasks_information")
        return {
            "total_unallocated_time": 0,
            "unallocated_task_count": 0,
            "assigned_working_hours": 0,
            "assigned_task_count": 0,
            "total_available_working_hours": 0
        }





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



# custom_app/pankaj.py

@frappe.whitelist()
def add_work_log_entry(task_name, start_time):
    task = frappe.get_doc("S Task", task_name)
    task.check_work_log = 1
    new_work_log = task.append("work_log_table", {
        "start_time": start_time,
        "logged_type":"Timer Generated",
    })
    task.save()
    frappe.db.commit()
    return {'work_log_entry_id': new_work_log.name}



# custom_app/pankaj.py

import frappe
from frappe.utils import get_datetime

@frappe.whitelist()
def update_work_log_entry(work_log_entry_id, end_time, duration, description):
    # print("sdffffffffff", work_log_entry_id, end_time, duration, description)
    # Convert the end_time to a datetime object
    end_time = get_datetime(end_time)
    # Calculate duration in hours
    duration_in_hours = float(duration) / 3600  # Ensure duration is a float
    print('duration_in_hourssssssssssssssss', duration_in_hours)
    try:
        # Update the work log entry
        frappe.db.set_value('S Task Work Log', work_log_entry_id, {
            'end_time': end_time,
            'duration': duration_in_hours,
            'description': description  # Add description
        })
        frappe.db.commit()
        return {'status': 'success', 'message': 'Work log entry updated successfully'}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Failed to update work log entry")
        return {'status': 'error', 'message': str(e)}







# import frappe
# from frappe.utils import nowdate

# @frappe.whitelist()
# def add_work_logs_to_timesheet_for_user(user):
#     today = nowdate()
    
#     # Fetch employee ID based on the user
#     employee_id = frappe.get_value('Employee', {'user_id': user}, 'name')
    
#     if not employee_id:
#         frappe.msgprint(f"No employee found for user {user}.")
#         return
    
#     # Fetch tasks assigned to the user
#     tasks = frappe.get_all(
#         'S Task',
#         filters={'users': ['like', f'%{user}%']},
#         fields=['name', 'project']
#     )
    
#     if not tasks:
#         frappe.msgprint(f"No tasks found for user {user}.")
#         return
    
#     # Initialize a dictionary to accumulate work logs by task and project
#     work_logs = {}
    
#     # Fetch work logs from work_log_table for each task
#     for task in tasks:
#         task_work_logs = frappe.get_all(
#             'S Task Work Log',
#             filters={'parent': task['name']},
#             fields=['start_time', 'end_time', 'duration', 'description']
#         )
        
#         for log in task_work_logs:
#             task_id = task['name']
#             project_name = task['project']
            
#             if (task_id, project_name) not in work_logs:
#                 work_logs[(task_id, project_name)] = {
#                     'task_id': task_id,
#                     'project_name': project_name,
#                     'duration': 0,
#                     'description': ''
#                 }
            
#             work_logs[(task_id, project_name)]['duration'] += log['duration']
#             if log['description']:
#                 # Append description if it's not empty
#                 if work_logs[(task_id, project_name)]['description']:
#                     work_logs[(task_id, project_name)]['description'] += " | " + log['description']
#                 else:
#                     work_logs[(task_id, project_name)]['description'] = log['description']
    
#     if not work_logs:
#         frappe.msgprint(f"No work logs found for tasks assigned to user {user}.")
#         return
    
#     # Check if a timesheet for today already exists
#     existing_timesheet = frappe.get_all(
#         'S Timesheet',
#         filters={'employee': employee_id, 'date': today},
#         fields=['name']
#     )
    
#     if existing_timesheet:
#         # Load the existing timesheet document
#         timesheet = frappe.get_doc('S Timesheet', existing_timesheet[0]['name'])
        
#         # Update existing timesheet
#         for log in work_logs.values():
#             log_exists = False
            
#             for time_log in timesheet.time_logs:
#                 if time_log.task == log['task_id']:
#                     # Update hours
#                     time_log.hours = log['duration']
#                     # Append description if it's not empty
#                     if log['description']:
#                         if time_log.description:
#                             time_log.description += " | " + log['description']
#                         else:
#                             time_log.description = log['description']
#                     # Ensure from_work_log is set to 1
#                     time_log.from_work_log = 1
#                     log_exists = True
#                     break
            
#             if not log_exists:
#                 timesheet.append('time_logs', {
#                     'activity_type': 'Execution',  # Replace with your actual activity type
#                     'hours': log['duration'],
#                     'task': log['task_id'],
#                     'project': log['project_name'],
#                     'description': log['description'],
#                     'from_work_log': 1
#                 })
        
#         # Save the updated timesheet
#         timesheet.save()
#         frappe.db.commit()
#         frappe.msgprint(f"Work logs updated in timesheet for user {user}.")
    
#     else:
#         # Create a new timesheet document
#         timesheet = frappe.get_doc({
#             'doctype': 'S Timesheet',
#             'employee': employee_id,
#             'date': today,
#             'time_logs': []
#         })
        
#         # Add merged work logs to the new timesheet
#         for log in work_logs.values():
#             project_exists = frappe.db.exists('S Project', log['project_name'])
#             task_exists = frappe.db.exists('S Task', log['task_id'])
            
#             if not project_exists:
#                 frappe.msgprint(f"Project {log['project_name']} does not exist.")
#             if not task_exists:
#                 frappe.msgprint(f"Task {log['task_id']} does not exist.")
            
#             if project_exists and task_exists:
#                 timesheet.append('time_logs', {
#                     'activity_type': 'Execution',  # Replace with your actual activity type
#                     'hours': log['duration'],
#                     'task': log['task_id'],
#                     'project': log['project_name'],
#                     'description': log['description'],
#                     'from_work_log': 1
#                 })
#             else:
#                 frappe.msgprint(f"Invalid project or task for log: {log}")

#         if not timesheet.time_logs:
#             frappe.msgprint("No valid work logs to add to the timesheet.")
#             return
        
#         # Insert the new timesheet document
#         timesheet.insert()
#         frappe.db.commit()
#         frappe.msgprint(f"Work logs added to new timesheet for user {user}.")





import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def add_work_logs_to_timesheet_for_user(user,date):
    today = date
    
    # Fetch employee ID based on the user
    employee_id = frappe.get_value('Employee', {'user_id': user}, 'name')
    
    if not employee_id:
        frappe.msgprint(f"No employee found for user {user}.")
        return
    
    # Fetch tasks assigned to the user
    tasks = frappe.get_all(
        'S Task',
        filters={'users': ['like', f'%{user}%']},
        fields=['name', 'project']
    )
    
    if not tasks:
        frappe.msgprint(f"No tasks found for user {user}.")
        return
    
    # Initialize a dictionary to accumulate work logs by task and project
    work_logs = {}
    
    # Fetch work logs from work_log_table for each task
    for task in tasks:
        task_work_logs = frappe.get_all(
            'S Task Work Log',
            filters={'parent': task['name'], 'date_time': today, 'deleted': 0, 'user': user},
            fields=['start_time', 'end_time', 'duration', 'description', 'name']
        )
        
        for log in task_work_logs:
            task_id = task['name']
            project_name = task['project']
            
            if (task_id, project_name) not in work_logs:
                work_logs[(task_id, project_name)] = {
                    'task_id': task_id,
                    'project_name': project_name,
                    'duration': 0,
                    'description': '',
                    'work_log_ids': []
                }
            
            work_logs[(task_id, project_name)]['duration'] += log['duration']
            work_logs[(task_id, project_name)]['work_log_ids'].append(log['name'])
            
            # Append description if it's not empty and avoid duplicates
            if log['description']:
                if work_logs[(task_id, project_name)]['description']:
                    descriptions = set(work_logs[(task_id, project_name)]['description'].split(" | "))
                    descriptions.add(log['description'])
                    work_logs[(task_id, project_name)]['description'] = " | ".join(descriptions)
                else:
                    work_logs[(task_id, project_name)]['description'] = log['description']
    
    if not work_logs:
        frappe.msgprint(f"No work logs found for tasks assigned to user {user}.")
        return
    
    # Check if a timesheet for today already exists
    existing_timesheet = frappe.get_all(
        'S Timesheet',
        filters={'employee': employee_id, 'date': today,'docstatus':0},
        fields=['name']
    )
    
    if existing_timesheet:
        # Load the existing timesheet document
        timesheet = frappe.get_doc('S Timesheet', existing_timesheet[0]['name'])
        
        # Update existing timesheet
        for log in work_logs.values():
            log_exists = False
            
            for time_log in timesheet.time_logs:
                if time_log.task == log['task_id']:
                    # Update hours
                    time_log.hours = log['duration']
                    # Append description if it's not empty
                    if log['description']:
                        if time_log.description:
                            descriptions = set(time_log.description.split(" | "))
                            descriptions.add(log['description'])
                            time_log.description = " | ".join(descriptions)
                        else:
                            time_log.description = log['description']
                    # Ensure from_work_log is set to 1
                    time_log.from_work_log = 1
                    # Append work log IDs
                    if time_log.work_log_id:
                        existing_work_log_ids = time_log.work_log_id.split(',')
                        updated_work_log_ids = set(existing_work_log_ids + log['work_log_ids'])
                        time_log.work_log_id = ','.join(updated_work_log_ids)
                    else:
                        time_log.work_log_id = ','.join(log['work_log_ids'])
                    log_exists = True
                    break
            
            if not log_exists:
                timesheet.append('time_logs', {
                    'activity_type': 'Execution',  # Replace with your actual activity type
                    'hours': log['duration'],
                    'task': log['task_id'],
                    'project': log['project_name'],
                    'description': log['description'],
                    'from_work_log': 1,
                    'work_log_id': ','.join(log['work_log_ids'])  # Join work_log_ids into a comma-separated string
                })
        
        # Save the updated timesheet
        timesheet.save()
        frappe.db.commit()
        frappe.msgprint(f"Work logs updated in timesheet for user {user}.")
    
    else:
        # Create a new timesheet document
        timesheet = frappe.get_doc({
            'doctype': 'S Timesheet',
            'employee': employee_id,
            'date': today,
            'time_logs': []
        })
        
        # Add merged work logs to the new timesheet
        for log in work_logs.values():
            project_exists = frappe.db.exists('S Project', log['project_name'])
            task_exists = frappe.db.exists('S Task', log['task_id'])
            
            if not project_exists:
                frappe.msgprint(f"Project {log['project_name']} does not exist.")
            if not task_exists:
                frappe.msgprint(f"Task {log['task_id']} does not exist.")
            
            if project_exists and task_exists:
                timesheet.append('time_logs', {
                    'activity_type': 'Execution',  # Replace with your actual activity type
                    'hours': log['duration'],
                    'task': log['task_id'],
                    'project': log['project_name'],
                    'description': log['description'],
                    'from_work_log': 1,
                    'work_log_id': ','.join(log['work_log_ids'])  # Join work_log_ids into a comma-separated string
                })
            else:
                frappe.msgprint(f"Invalid project or task for log: {log}")

        if not timesheet.time_logs:
            frappe.msgprint("No valid work logs to add to the timesheet.")
            return
        
        # Insert the new timesheet document
        timesheet.insert()
        frappe.db.commit()
        frappe.msgprint(f"Work logs added to new timesheet for user {user}.")



# import frappe
# from frappe.utils import nowdate

# @frappe.whitelist()
# def add_work_logs_to_timesheet_for_user(user,date):
#     today = date
    
#     # Fetch employee ID based on the user
#     employee_id = frappe.get_value('Employee', {'user_id': user}, 'name')
    
#     if not employee_id:
#         frappe.msgprint(f"No employee found for user {user}.")
#         return
    
#     # Fetch tasks assigned to the user
#     tasks = frappe.get_all(
#         'S Task',
#         # filters={'users': ['like', f'%{user}%']},
#         fields=['name', 'project']
#     )
    
#     if not tasks:
#         frappe.msgprint(f"No tasks found for user {user}.")
#         return
    
#     # Initialize a dictionary to accumulate work logs by task and project
#     work_logs = {}
    
#     # Fetch work logs from work_log_table for each task
#     for task in tasks:
#         task_work_logs = frappe.get_all(
#             'S Task Work Log',
#             filters={'parent': task['name'], 'date_time': today, 'deleted': 0, 'user': user},
#             fields=['start_time', 'end_time', 'duration', 'description', 'name']
#         )
        
#         for log in task_work_logs:
#             task_id = task['name']
#             project_name = task['project']
            
#             if (task_id, project_name) not in work_logs:
#                 work_logs[(task_id, project_name)] = {
#                     'task_id': task_id,
#                     'project_name': project_name,
#                     'duration': 0,
#                     'description': '',
#                     'work_log_ids': []
#                 }
            
#             work_logs[(task_id, project_name)]['duration'] += log['duration']
#             work_logs[(task_id, project_name)]['work_log_ids'].append(log['name'])
            
#             # Append description if it's not empty and avoid duplicates
#             if log['description']:
#                 if work_logs[(task_id, project_name)]['description']:
#                     descriptions = set(work_logs[(task_id, project_name)]['description'].split(" | "))
#                     descriptions.add(log['description'])
#                     work_logs[(task_id, project_name)]['description'] = " | ".join(descriptions)
#                 else:
#                     work_logs[(task_id, project_name)]['description'] = log['description']
    
#     if not work_logs:
#         frappe.msgprint(f"No work logs found for tasks assigned to user {user}.")
#         return
    
#     # Check if a timesheet for today already exists
#     existing_timesheet = frappe.get_all(
#         'S Timesheet',
#         filters={'employee': employee_id, 'date': today,'docstatus':0},
#         fields=['name']
#     )
    
#     if existing_timesheet:
#         # Load the existing timesheet document
#         timesheet = frappe.get_doc('S Timesheet', existing_timesheet[0]['name'])
        
#         # Update existing timesheet
#         for log in work_logs.values():
#             log_exists = False
            
#             for time_log in timesheet.time_logs:
#                 if time_log.task == log['task_id']:
#                     # Update hours
#                     time_log.hours = log['duration']
#                     # Append description if it's not empty
#                     if log['description']:
#                         if time_log.description:
#                             descriptions = set(time_log.description.split(" | "))
#                             descriptions.add(log['description'])
#                             time_log.description = " | ".join(descriptions)
#                         else:
#                             time_log.description = log['description']
#                     # Ensure from_work_log is set to 1
#                     time_log.from_work_log = 1
#                     # Append work log IDs
#                     if time_log.work_log_id:
#                         existing_work_log_ids = time_log.work_log_id.split(',')
#                         updated_work_log_ids = set(existing_work_log_ids + log['work_log_ids'])
#                         time_log.work_log_id = ','.join(updated_work_log_ids)
#                     else:
#                         time_log.work_log_id = ','.join(log['work_log_ids'])
#                     log_exists = True
#                     break
            
#             if not log_exists:
#                 timesheet.append('time_logs', {
#                     'activity_type': 'Execution',  # Replace with your actual activity type
#                     'hours': log['duration'],
#                     'task': log['task_id'],
#                     'project': log['project_name'],
#                     'description': log['description'],
#                     'from_work_log': 1,
#                     'work_log_id': ','.join(log['work_log_ids'])  # Join work_log_ids into a comma-separated string
#                 })
        
#         # Save the updated timesheet
#         timesheet.save()
#         frappe.db.commit()
#         frappe.msgprint(f"Work logs updated in timesheet for user {user}.")
    
#     else:
#         # Create a new timesheet document
#         timesheet = frappe.get_doc({
#             'doctype': 'S Timesheet',
#             'employee': employee_id,
#             'date': today,
#             'time_logs': []
#         })
        
#         # Add merged work logs to the new timesheet
#         for log in work_logs.values():
#             project_exists = frappe.db.exists('S Project', log['project_name'])
#             task_exists = frappe.db.exists('S Task', log['task_id'])
            
#             if not project_exists:
#                 frappe.msgprint(f"Project {log['project_name']} does not exist.")
#             if not task_exists:
#                 frappe.msgprint(f"Task {log['task_id']} does not exist.")
            
#             if project_exists and task_exists:
#                 timesheet.append('time_logs', {
#                     'activity_type': 'Execution',  # Replace with your actual activity type
#                     'hours': log['duration'],
#                     'task': log['task_id'],
#                     'project': log['project_name'],
#                     'description': log['description'],
#                     'from_work_log': 1,
#                     'work_log_id': ','.join(log['work_log_ids'])  # Join work_log_ids into a comma-separated string
#                 })
#             else:
#                 frappe.msgprint(f"Invalid project or task for log: {log}")

#         if not timesheet.time_logs:
#             frappe.msgprint("No valid work logs to add to the timesheet.")
#             return
        
#         # Insert the new timesheet document
#         timesheet.insert()
#         frappe.db.commit()
#         frappe.msgprint(f"Work logs added to new timesheet for user {user}.")



@frappe.whitelist()
def get_task_subject(task_name):
    task = frappe.get_all('S Task', filters={'name': task_name}, fields=['subject', 'name'])
    if task:
        task_data = task[0]
        task_data['url'] = frappe.utils.get_url_to_form('S Task', task_data['name'])
        return task_data
    else:
        return {}



import frappe
from frappe import _

@frappe.whitelist()
def check_permission_for_deletion(user, row):
    roles = frappe.get_all('Has Role', filters={'parent': user}, fields=['role'])
    role_names = [r.role for r in roles]
    if 'System Manager' in role_names:
        return {'has_permission': True}
    
    # If permission is not granted, return row data along with permission status
    return {'has_permission': False, 'row': row}

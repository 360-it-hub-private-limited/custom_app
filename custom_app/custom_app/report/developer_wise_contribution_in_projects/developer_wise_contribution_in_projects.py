import frappe

def execute(filters=None):
    columns = [
        {"label": "Project Name", "fieldname": "project_name", "fieldtype": "Link", "options": "S Project", "width": 200},
        {"label": "Total Estimated Hours (hrs)", "fieldname": "total_estimated_hours", "fieldtype": "Float", "width": 200},
        {"label": "Total Assigned Hours (hrs)", "fieldname": "total_assigned_hours", "fieldtype": "Float", "width": 200},
        {"label": "Completed Estimated Hours (hrs)", "fieldname": "completed_hours", "fieldtype": "Float", "width": 200},
        {"label": "Completed %", "fieldname": "completed_percentage", "fieldtype": "Percent", "width": 150},
        {"label": "Total Contribution (%)", "fieldname": "total_contribution", "fieldtype": "Percent", "width": 150},
        {"label": "Assigned Tasks Count", "fieldname": "assigned_tasks_count", "fieldtype": "Int", "width": 150},
        {"label": "Overtime Tasks Count", "fieldname": "overtime_tasks_count", "fieldtype": "Int", "width": 150},
        {"label": "Overtime Estimated Hours (hrs)", "fieldname": "overtime_hours", "fieldtype": "Float", "width": 200},
        {"label": "Saved Time Tasks Count", "fieldname": "saved_time_tasks_count", "fieldtype": "Int", "width": 150},
        {"label": "Saved Time Estimated Hours (hrs)", "fieldname": "saved_time_hours", "fieldtype": "Float", "width": 200},
    ]

    data = []

    if filters:
        employee = filters.get("employee")

        if employee:
            # Fetch the user_id of the selected employee
            user_id = frappe.get_value('Employee', employee, 'user_id')

            # Fetch all projects
            projects = frappe.get_all('S Project', fields=['name'])

            for project in projects:
                project_name = project['name']
                project_doc = frappe.get_doc('S Project', project_name)

                if project_doc:
                    # Access the table field 'userss'
                    userss = project_doc.get('userss') or []

                    # Extract user values from each row
                    project_users = [row.user for row in userss if row.user]

                    if user_id in project_users:
                        # Fetch all tasks related to this project
                        tasks = frappe.get_all('S Task', filters={'project': project_name}, fields=['expected_time', 'actual_time', 'users', 'task_status'])

                        # Initialize metrics
                        total_estimated_hours = 0
                        total_assigned_hours = 0
                        completed_hours = 0
                        assigned_tasks_count = 0
                        overtime_task_count = 0
                        overtime_hours = 0
                        saved_time_task_count = 0
                        saved_time_hours = 0

                        # Calculate metrics
                        for task in tasks:
                            expected_time = task.get('expected_time', 0)
                            actual_time = task.get('actual_time', 0)
                            assigned_users = task.get('users') or []
                            task_status = task.get('task_status')

                            total_estimated_hours += expected_time

                            if user_id in assigned_users:
                                total_assigned_hours += expected_time
                                assigned_tasks_count += 1

                                if actual_time is not None:
                                    if task_status == 'Completed':
                                        completed_hours += expected_time
                                        if actual_time > expected_time:
                                            overtime_task_count += 1
                                            overtime_hours += (actual_time - expected_time)
                                        elif actual_time < expected_time:
                                            saved_time_task_count += 1
                                            saved_time_hours += (expected_time - actual_time)

                        completed_percentage = (completed_hours / total_assigned_hours) * 100 if total_assigned_hours != 0 else 0
                        total_contribution = (total_assigned_hours / total_estimated_hours) * 100 if total_estimated_hours != 0 else 0

                        # Append the data for this project
                        data.append({
                            'project_name': project_name,
                            'total_estimated_hours': total_estimated_hours,
                            'total_assigned_hours': total_assigned_hours,
                            'completed_hours': completed_hours,
                            'completed_percentage': completed_percentage,
                            'total_contribution': total_contribution,
                            'assigned_tasks_count': assigned_tasks_count,
                            'overtime_tasks_count': overtime_task_count,
                            'overtime_hours': overtime_hours,
                            'saved_time_tasks_count': saved_time_task_count,
                            'saved_time_hours': saved_time_hours
                        })

    # Format the data for display
    formatted_data = [
        {
            'project_name': row['project_name'],
            'total_estimated_hours': f"{row['total_estimated_hours']} hrs",
            'total_assigned_hours': f"{row['total_assigned_hours']} hrs",
            'completed_hours': f"{row['completed_hours']} hrs",
            'completed_percentage': row['completed_percentage'],
            'total_contribution': row['total_contribution'],
            'assigned_tasks_count': row['assigned_tasks_count'],
            'overtime_tasks_count': row['overtime_tasks_count'],
            'overtime_hours': f"{row['overtime_hours']} hrs",
            'saved_time_tasks_count': row['saved_time_tasks_count'],
            'saved_time_hours': f"{row['saved_time_hours']} hrs"
        }
        for row in data
    ]

    return columns, formatted_data

# Copyright (c) 2024, pankaj@360ithub.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class STaskWorkLog(Document):
    pass
	# def on_trash(self):
	# 	print('deleteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
	# 	# # Get the current user
	# 	# current_user = frappe.session.user
		
	# 	# # Check if the current user has the role 'System Manager'
	# 	# if 'System Manager' not in frappe.get_roles(current_user):
	# 	frappe.throw("Only users with the 'System Manager' role can delete records.")
	
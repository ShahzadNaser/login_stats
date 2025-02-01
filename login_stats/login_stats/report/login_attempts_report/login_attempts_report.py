# Copyright (c) 2025, Shahzad Naser and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate,get_datetime


def execute(filters=None):
	""" This method 'll prepare data and sent back to UI for viewing"""
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	""" Prepare Columns for Report """
	columns = [
		{
			"label": _("Full Name"),
			"fieldtype": "Data",
			"fieldname": "full_name",
			"width": 200,
		},
		{
			"label": _("User"),
			"fieldtype": "Data",
			"fieldname": "user",
			"width": 250,
		},
		{
			"label": _("Login Attempts"),
			"fieldtype": "Int",
			"fieldname": "login_attempts",
			"width": 160,
		},
	]

	return columns

def get_conditions(filters):
	""" Generate Condition on bases of filters """
	conditions = {}
	if filters.get("from_date") or filters.get("to_date"):
		conditions["communication_date"] = ["between",[get_datetime(getdate(filters.get("from_date"))),get_datetime("{} 23:59:59".format(getdate(filters.get("to_date"))))]]
	return conditions

def get_data(filters):
	""" Get data from system as per the filters"""
	conditions = get_conditions(filters)
	return frappe.get_all(
        "Activity Log",
        filters=conditions,
        fields=["full_name", "user", "count(*) as login_attempts"],
        group_by="user"
    )

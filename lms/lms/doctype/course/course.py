# Copyright (c) 2026, Mohammed Almatrafi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Course(Document):
    def validate(self):
    if self.maximum_students is not None and self.maximum_students <= 0:
        frappe.throw(frappe._("Maximum Students must be greater than zero."))

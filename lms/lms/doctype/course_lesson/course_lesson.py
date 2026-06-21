# Copyright (c) 2026, Mohammed Almatrafi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CourseLesson(Document):
    def validate(self):
        if not self.duration:
            default_duration = frappe.db.get_single_value("LMS Settings", "default_course_duration")
            if default_duration:
                self.duration = default_duration

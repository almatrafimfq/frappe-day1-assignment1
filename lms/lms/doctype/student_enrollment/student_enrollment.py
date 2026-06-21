# Copyright (c) 2026, Mohammed Almatrafi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class StudentEnrollment(Document):
    def before_insert(self):
    self.enrollment_date = today()

    def validate(self):
        self.validate_max_students()
        self.validate_self_enrollment()

    def validate_max_students(self):
        max_students = frappe.db.get_value("Course", self.course, "maximum_students")
        if max_students:
            current_count = frappe.db.count(
                "Student Enrollment",
                {"course": self.course, "name": ["!=", self.name]}
            )
            if current_count >= max_students:
                frappe.throw(frappe._("This course has reached its maximum number of students."))

    def validate_self_enrollment(self):
        allow_self_enrollment = frappe.db.get_single_value("LMS Settings", "allow_self_enrollment")
        if not allow_self_enrollment:
            if self.student == frappe.session.user:
                frappe.throw(frappe._("You are not allowed to enroll yourself in this course."))

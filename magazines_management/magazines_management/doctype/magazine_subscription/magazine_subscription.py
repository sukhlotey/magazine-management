# Copyright (c) 2025, Sukhpreet Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class MagazineSubscription(Document):

    def before_submit(self):
        exists = frappe.db.exists(
            "Magazine Subscription",
            {
                "magazine_reader": self.magazine_reader,
                "docstatus": DocStatus.submitted(),
                # Check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active subscription for this member.")




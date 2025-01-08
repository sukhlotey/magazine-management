import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class MagazineTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            # Set the magazine status to "Issued"
            magazine = frappe.get_doc("Magazine", self.magazine)
            magazine.status = "Issued"
            magazine.save()

        elif self.type == "Return":
            self.validate_return()
            # Set the magazine status to "Available"
            magazine = frappe.get_doc("Magazine", self.magazine)
            magazine.status = "Available"
            magazine.save()

    def validate_issue(self):
        self.validate_membership()
        magazine = frappe.get_doc("Magazine", self.magazine)
        # Magazine cannot be issued if it is already issued
        if magazine.status == "Issued":
            frappe.throw("Magazine is already issued by another member")

    def validate_return(self):
        magazine = frappe.get_doc("Magazine", self.magazine)
        # Magazine cannot be returned if it is not issued first
        if magazine.status == "Available":
            frappe.throw("Magazine cannot be returned without being issued first")

    def validate_membership(self):
        # Check if a valid membership exists for this library member
        valid_membership = frappe.db.exists(
            "Magazine Subscription",
            {
                "magazine_reader": self.magazine_reader,
                "docstatus": DocStatus.submitted(),
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")


# import frappe
from frappe.model.document import Document


class MagazineReader(Document):
     def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'


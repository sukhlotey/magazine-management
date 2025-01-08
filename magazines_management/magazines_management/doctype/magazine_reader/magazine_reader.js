frappe.ui.form.on('Magazine Reader', {
    refresh: function (frm) {
        // Add button to create a new Magazine Subscription
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Magazine Subscription', {
                magazine_reader: frm.doc.name
            });
        });

        // Add button to create a new Magazine Transaction
        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Magazine Transaction', {
                magazine_reader: frm.doc.name
            });
        });
    }
});

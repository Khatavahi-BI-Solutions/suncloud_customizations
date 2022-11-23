import frappe

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def lead_query(doctype, txt, searchfield, start, page_len, filters):
    customer = filters['customer']
    data = frappe.db.sql(""" 
    select 
        lead_name,
        lead_name1,
        lead_name2,
        lead_name3,
        lead_name4 
    from 
        `tabcustomer` 
    where 
        name = %(customer)s
    """,
    {
        'customer':customer
    })
    data = [data[0]['lead_name'],data[0]['lead_name1'],data[0]['lead_name2'],data[0]['lead_name3'],data[0]['lead_name4']]
    return data
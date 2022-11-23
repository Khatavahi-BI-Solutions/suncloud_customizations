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
        `tabCustomer` 
    where 
        name = %(customer)s
    """,
    {
        'customer':customer
    }, as_dict=True)
    finaldata = []
    if data[0]['lead_name']:
        finaldata.append([data[0]['lead_name'],])
    if data[0]['lead_name1']:
        finaldata.append([data[0]['lead_name1'],])
    if data[0]['lead_name2']:
        finaldata.append([data[0]['lead_name2'],])
    if data[0]['lead_name3']:
        finaldata.append([data[0]['lead_name3'],])
    if data[0]['lead_name4']:
        finaldata.append([data[0]['lead_name4'],])    
    return finaldata

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def quotation_query(doctype, txt, searchfield, start, page_len, filters):
    customer = filters['customer']
    data = frappe.db.sql(""" 
    select 
        referencia_da_proposta,
        referencia_da_proposta1,
        referencia_da_proposta2,
        referencia_da_proposta3,
        referencia_da_proposta4 
    from 
        `tabCustomer` 
    where 
        name = %(customer)s
    """,
    {
        'customer':customer
    }, as_dict=True)
    finaldata = []
    if data[0]['referencia_da_proposta']:
        finaldata.append([data[0]['referencia_da_proposta'],])
    if data[0]['referencia_da_proposta1']:
        finaldata.append([data[0]['referencia_da_proposta1'],])
    if data[0]['referencia_da_proposta2']:
        finaldata.append([data[0]['referencia_da_proposta2'],])
    if data[0]['referencia_da_proposta3']:
        finaldata.append([data[0]['referencia_da_proposta3'],])
    if data[0]['referencia_da_proposta4']:
        finaldata.append([data[0]['referencia_da_proposta4'],])    
    return finaldata
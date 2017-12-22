from odoo import models, fields, api

class Customer(models.Model):
    _name = 'modulex.customer'
    name = fields.Text(required = True)
    phone = fields.Char()
    mobile = fields.Char(required = True)
    company_name = fields.Text(required = True)
    notes = fields.Text()
    email = fields.Text()
    website = fields.Text()
    address = fields.Text()
    job_position = fields.Text()

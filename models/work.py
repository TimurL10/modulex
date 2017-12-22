from Odoo import models,api

class Work(models.Model):
    name = fields.Text(required = True)
    category = fields.Text(required = True)
    start_date = field.Char(required = True)
    end_date = field.Char()
    status = field.Char()
    description = field.Char()

from odoo import api, fields, models, _
from datetime import datetime

class HausTaskRO(models.Model):
    _name = "haus.task"
    _description = "Haus Schedule Route Optimization Platform"

    flow = fields.Selection([
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup')
    ], string="Flow", required=True)
    
 
    assignee = fields.Char(string='Assignee')
    
    customer_name = fields.Char(string='Customer Name', invisible=True)
    customer_address = fields.Text(string='Customer Address',invisible=True, widget='text', attrs={'rows': 8, 'cols': 75} )
    customer_coordinate = fields.Char(string='Customer Coordinate', invisible=True)

    requester_name = fields.Char(string='Requester Name', invisible=True)
    requester_address = fields.Text(string='Requester Address',invisible=True, widget='text', attrs={'rows': 10, 'cols': 100} )
    pickup_point_coordinate = fields.Char(string='Pickup Point Coordinate', invisible=True)
    
    start_time = fields.Date(String="Start Time",  invisible=True, default=datetime.today())
    end_time = fields.Date(String="End Time", invisible=True)
    custom_title = fields.Char(string='Custom Title', compute='_compute_custom_title')

    status = fields.Selection([
        ('ongoing', 'Sedang Berjalan'),
        ('done', 'Selesai'),
        ('cancelled', 'Dibatalkan')
    ], string='Status', store=True, track_visibility='onchange', default='ongoing')


    @api.onchange('flow')
    def _onchange_flow(self):
        if self.flow == 'delivery':
            self.customer_name = False  
        else:
            self.customer_name = True  
    

    @api.depends('flow', 'requester_name', 'customer_name')
    def _compute_custom_title(self):
        for record in self:
            if record.flow == 'pickup':
                record.custom_title = record.requester_name
            elif record.flow == 'delivery':
                record.custom_title = record.customer_name
            else:
                record.custom_title = ""
                 
    def action_done(self):
        self.write({'status': 'done'})
    def action_cancel(self):
        self.write({'status': 'cancelled'})

# -*- coding: utf-8 -*-



from odoo import http, _
# zob. addons/website_event/controllers/main.py
from odoo.addons.website_event.controllers.main import WebsiteEventController
from odoo.http import request


class WebsiteEventFront3Controller(WebsiteEventController):

    @http.route(['/front3',], type='http', auth="public", website=True)
    def front3(self, **param):
        Event = request.env['event.event']
        events = Event.search([])
        values = {
            'events': events,
        }
        return request.render("front3.front0", values)



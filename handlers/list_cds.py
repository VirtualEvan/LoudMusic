from classes.cd import CD

import webapp2
from evironment import render


class ListCDsHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title": "CD List",
            "cds": CD.query(),
            "content": "list_cds"
        }

        render(self, template_values)

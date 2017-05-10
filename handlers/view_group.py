from classes.group import Group

import webapp2
from evironment import render


class ViewGroupHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title": "View Group",
            "group": Group.get_by_id(int(self.request.get("id"))),
            "content": "view_group"
        }

        render(self, template_values)

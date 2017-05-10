from classes.cd import Group

import webapp2
from evironment import render


class ListGroupsHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title": "Group List",
            "groups": Group.query(),
            "content": "list_groups"
        }

        render(self, template_values)

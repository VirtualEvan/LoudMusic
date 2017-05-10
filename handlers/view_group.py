from google.appengine.api import users
from google.appengine.ext import ndb

from classes.group import Group
from classes.cd import CD
from datetime import datetime
import time

import webapp2
from evironment import render


class ViewHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title": "View",
            "group": Group.get_by_id(int(self.request.get("id"))),
            "content": "view"
        }
        print(template_values)

        render(self, template_values)

from google.appengine.api import users
from google.appengine.ext import ndb

from classes.cd import CD

import webapp2
from evironment import JINJA_ENVIRONMENT, render


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "user_name": users.get_current_user().nickname(),
            "content": "home"
        }

        render(self, "home", template_values)

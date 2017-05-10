from google.appengine.api import users
from google.appengine.ext import ndb

from classes.cd import CD

import webapp2
from evironment import render


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title": "Home",
            "content": "home"
        }

        render(self, template_values)

from google.appengine.api import users
from google.appengine.ext import ndb

from classes.cd import CD

import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user is not None:
            user_name = user.nickname()
            access_link = users.create_logout_url("/")
            series = CD.query(CD.user == user.user_id()).order(CD.added)

            template_values = {
                "user_name": user_name,
                "access_link": access_link,
                "series": series,
            }

            template = JINJA_ENVIRONMENT.get_template("home.html")
            self.response.write(template.render(template_values));
        else:
            self.redirect("/")

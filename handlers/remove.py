from google.appengine.ext import ndb

from google.appengine.api import users

import webapp2
import time


class RemoveHandler(webapp2.RequestHandler):
    def get(self):
        try:
            key = self.request.get("key")
        except:
            key = None

        if key is None:
            self.redirect("/error?msg=Missing key")
            return

        try:
            obj = ndb.Key(urlsafe=key).get()
        except:
            self.redirect("/error?msg=Comment was not found")
            return

        if users.get_current_user() and obj.user == users.get_current_user().email():
            obj.key.delete()
            time.sleep(1)
            self.redirect("/home")

        else:
            self.redirect("/")

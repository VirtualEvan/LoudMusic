from google.appengine.ext import ndb

from google.appengine.api import users

import webapp2
import time


class RemoveHandler(webapp2.RequestHandler):
    def get(self):
        try:
            comment_key = self.request.get("key")
        except:
            comment_key = None

        if comment_key is None:
            self.redirect("/error?msg=Missing key")
            return

        try:
            comment = ndb.Key(urlsafe=comment_key).get()
        except:
            self.redirect("/error?msg=Comment was not found")
            return

        if users.get_current_user() and comment.user == users.get_current_user().email():
            comment.key.delete()
            time.sleep(1)
            self.redirect("/home")

        else:
            self.redirect("/")

from google.appengine.ext import ndb

from google.appengine.api import users

import webapp2
import time


class EditHandler(webapp2.RequestHandler):
    def post(self):
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
            comment.content = self.request.get("content")
            comment.stars = int(self.request.get("stars", 0))

            # Chk
            if len(comment.content) < 1:
                self.redirect("/error?msg=" + "Edit failed: Content is empty")
                return

            if comment.stars < 1 or comment.stars > 5:
                self.redirect("/error?msg=" + "Edit failed: Wrong rating")
                return

            comment.put()
            time.sleep(1)
            self.redirect("/home")

        else:
            self.redirect("/")

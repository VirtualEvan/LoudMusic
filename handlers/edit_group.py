from datetime import datetime
from google.appengine.ext import ndb

from google.appengine.api import users

import webapp2
import time

from classes.group import Group
from evironment import render


class EditGroupHandler(webapp2.RequestHandler):
    def get(self):
        group_key = ndb.Key(urlsafe=self.request.get("key"))

        template_values = {
            "title": "Edit Group",
            "group": Group.get_by_id(group_key.id()),
            "content": "edit_group"
        }

        render(self, template_values)

    def post(self):
        try:
            group_key = self.request.get("key")
        except:
            group_key = None

        if group_key is None:
            self.redirect("/error?msg=Missing key")
            return

        try:
            group = ndb.Key(urlsafe=group_key).get()
        except:
            self.redirect("/error?msg=Comment was not found")
            return

        if users.get_current_user():
            group.name = self.request.get("name").strip()
            group.genre = self.request.get("genre").strip()
            group.foundation_date = datetime.strptime(self.request.get("foundation_date").strip(), '%Y-%m-%d')
            group.members = self.request.get("members").strip()

            # Chk
            if len(group.name) < 1:
                self.redirect("/error?msg=" + "Couldn't add group: Group name is mandatory")
                return
            if len(group.genre) < 1:
                self.redirect("/error?msg=" + "Couldn't add group: Group genre is mandatory")
                return
            if group.foundation_date > datetime.now():
                self.redirect("/error?msg=" + "Couldn't add group: Invalid date")
                return
            if len(group.members) < 1:
                self.redirect("/error?msg=" + "Couldn't add group: Group members are mandatory")
                return

            # Save
            group.put()
            time.sleep(1)
            self.redirect("/list_groups")

        else:
            self.redirect("/")

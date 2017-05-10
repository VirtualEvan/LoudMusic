from datetime import datetime
from google.appengine.ext import ndb

from google.appengine.api import users

import webapp2
import time

from classes.cd import CD
from classes.group import Group
from evironment import render


class EditCDHandler(webapp2.RequestHandler):
    def get(self):
        cd_key = ndb.Key(urlsafe=self.request.get("key"))

        template_values = {
            "title": "Edit CD",
            "cd": CD.get_by_id(cd_key.id()),
            "groups": Group.query(),
            "content": "edit_cd"
        }

        render(self, template_values)

    def post(self):
        try:
            cd_key = self.request.get("key")
        except:
            cd_key = None

        if cd_key is None:
            self.redirect("/error?msg=Missing key")
            return

        try:
            cd = ndb.Key(urlsafe=cd_key).get()
        except:
            self.redirect("/error?msg=Comment was not found")
            return

        if users.get_current_user():
            cd.title = self.request.get("title").strip()
            cd.record_company = self.request.get("record_company").strip()
            cd.group = ndb.Key(urlsafe=self.request.get("group"))
            cd.description = self.request.get("description").strip()

            # Chk
            if len(cd.title) < 1:
                self.redirect("/error?msg=" + "Couldn't add CD: CD title is mandatory")
                return
            if len(cd.record_company) < 1:
                self.redirect("/error?msg=" + "Couldn't add CD: CD record company is mandatory")
                return

            if Group.query(ancestor=cd.group).fetch() is None:
                self.redirect("/error?msg=" + "Couldn't add CD: Specified group does not exist")
                return
            if len(cd.description) < 1:
                self.redirect("/error?msg=" + "Couldn't add CD: Description is mandatory")
                return

            if not self.request.get("publication_date"):
                self.redirect("/error?msg=" + "Couldn't add CD: Invalid publication date")
                return

            cd.publication_date = datetime.strptime(self.request.get("publication_date").strip(), '%Y-%m-%d')

            if cd.publication_date > datetime.now():
                self.redirect("/error?msg=" + "Couldn't add CD: Invalid publication date")
                return

            if datetime.date(cd.publication_date) < cd.group.get().foundation_date:
                self.redirect("/error?msg=" + "Couldn't add CD: Publication date before group foundation")
                return

            # Save
            cd.put()
            time.sleep(1)
            self.redirect("/home")

        else:
            self.redirect("/")

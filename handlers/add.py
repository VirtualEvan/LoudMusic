from google.appengine.api import users
from google.appengine.ext import ndb

from classes.group import Group
from classes.cd import CD
from classes.comment import Comment
from datetime import datetime
import time

import webapp2
from evironment import render


class AddCDHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title": "Add CD",
            "groups": Group.query(),
            "content": "add_cd"
        }

        render(self, template_values)


class AddGroupHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "title": "Add Group",
            "content": "add_group"
        }

        render(self, template_values)


class AddHandler(webapp2.RequestHandler):
    def post(self):

        user = users.get_current_user()

        if user is None:
            self.redirect("/")

        else:
            if self.request.GET['type'] == "group":
                # Create group
                group = Group()
                group.user = user.email()
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

            elif self.request.GET['type'] == "cd":
                # Create cd
                cd = CD()
                cd.user = user.email()
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

            elif self.request.GET['type'] == "comment":
                # Create cd
                comment = Comment()
                comment.user = user.email()
                comment.content = self.request.get("new_comment").strip()
                comment.cd = ndb.Key(urlsafe=self.request.get("cd"))
                comment.stars = int(self.request.get("stars", 0))

                # Chk
                if CD.query(ancestor=comment.cd).fetch() is None:
                    self.redirect("/error?msg=" + "Couldn't add comment: Specified CD does not exist")
                    return
                if len(comment.content) < 1:
                    self.redirect("/error?msg=" + "Couldn't add comment: Content is empty")
                    return
                if comment.stars < 1 or comment.stars > 5:
                    self.redirect("/error?msg=" + "Edit failed: Wrong rating")
                    return

                # Save
                comment.put()

            else:
                self.redirect("/error?msg=" + "Invalid form")
                return

            time.sleep(1)
            self.redirect("/home")

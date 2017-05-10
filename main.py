#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import users
from evironment import JINJA_ENVIRONMENT

from handlers.home import HomeHandler
from handlers.add import AddHandler
from handlers.add import AddCDHandler
from handlers.add import AddGroupHandler
from handlers.list_cds import ListCDsHandler
from handlers.list_groups import ListGroupsHandler
from handlers.view_cd import ViewCDHandler
from handlers.view_group import ViewGroupHandler
from handlers.remove import RemoveHandler
from handlers.edit import EditHandler
from handlers.edit_cd import EditCDHandler
from handlers.edit_group import EditGroupHandler
from handlers.error import ErrorHandler


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user is None:
            template_values = {
                "title": "Login",
                "login": "Please login",
                "access_link": users.create_login_url("/home"),
                "content": "login"
            }

            template = JINJA_ENVIRONMENT.get_template("index.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/home")


app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/home', HomeHandler),
    ('/list_cds', ListCDsHandler),
    ('/list_groups', ListGroupsHandler),
    ('/view_cd', ViewCDHandler),
    ('/view_group', ViewGroupHandler),
    ('/add', AddHandler),
    ('/add_cd', AddCDHandler),
    ('/add_group', AddGroupHandler),
    ('/edit', EditHandler),
    ('/edit_cd', EditCDHandler),
    ('/edit_group', EditGroupHandler),
    ('/remove', RemoveHandler),
    ('/error', ErrorHandler)
], debug=True)

import os
import jinja2
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=["jinja2.ext.autoescape", "jinja2.ext.i18n"],
    autoescape=True)
JINJA_ENVIRONMENT.install_null_translations()


def render(self, redirect, template_values):
    user = users.get_current_user()
    if user is not None:
        # TODO: TO MANY REDIRECTS
        self.redirect("/"+redirect)
        return
    else:
        access_link = users.create_login_url("/"+redirect)

    template_values["access_link"] = access_link

    template = JINJA_ENVIRONMENT.get_template("index.html")
    self.response.write(template.render(template_values))

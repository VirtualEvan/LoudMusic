import os
import jinja2
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=["jinja2.ext.autoescape", "jinja2.ext.i18n"],
    autoescape=True)
JINJA_ENVIRONMENT.install_null_translations()


def render(target, template_values):
    user = users.get_current_user()

    if user is None:
        target.redirect("/")

    else:
        template_values["access_link"] = users.create_logout_url("/")
        template_values["user_name"] = users.get_current_user().nickname()
        template = JINJA_ENVIRONMENT.get_template("index.html")
        target.response.write(template.render(template_values))


def date_format(date):
    return date.strftime('%d-%m-%Y')


JINJA_ENVIRONMENT.filters['date_format'] = date_format

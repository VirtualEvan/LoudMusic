from google.appengine.ext import ndb
from classes.group import Group


class CD(ndb.Model):
    user = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    record_company = ndb.StringProperty(required=True)
    publication_date = ndb.DateProperty(required=True)
    group = ndb.KeyProperty(kind=Group, required=True)
    description = ndb.StringProperty(required=True)


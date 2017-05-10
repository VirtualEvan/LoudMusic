from google.appengine.ext import ndb


class Group(ndb.Model):
    user = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    genre = ndb.StringProperty(required=True)
    foundation_date = ndb.DateProperty(required=True)
    members = ndb.StringProperty(required=True)

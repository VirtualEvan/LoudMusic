from google.appengine.ext import ndb
from classes.cd import CD


class Comment(ndb.Model):
    user = ndb.StringProperty(required=True)
    content = ndb.StringProperty(required=True)
    cd = ndb.KeyProperty(kind=CD, required=True)
    date = ndb.DateProperty(auto_now_add=True)
    stars = ndb.IntegerProperty(required=True)


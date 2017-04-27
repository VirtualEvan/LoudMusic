from google.appengine.ext import ndb


class CD(ndb.Model):
    user = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    picture = ndb.StringProperty()
    added = ndb.DateProperty(auto_now_add=True)
    lastEpisode = ndb.IntegerProperty(required=True)
    web = ndb.StringProperty()
    comments = ndb.StringProperty()

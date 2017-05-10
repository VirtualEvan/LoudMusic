from google.appengine.ext import ndb

from classes.cd import CD
from classes.comment import Comment

import webapp2
from evironment import render


class ViewCDHandler(webapp2.RequestHandler):
    def get(self):
        cd_key = ndb.Key(urlsafe=self.request.get("key"))

        rating_list = []
        comments = Comment.query(Comment.cd == cd_key)
        for comment in comments:
            rating_list.append(comment.stars)
        average_rating = sum(rating_list) / max(len(rating_list), 1)

        template_values = {
            "title": "View CD",
            "cd": CD.get_by_id(cd_key.id()),
            "comments": comments,
            "content": "view_cd",
            "rating": average_rating
        }

        render(self, template_values)

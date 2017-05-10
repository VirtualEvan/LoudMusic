import webapp2
from evironment import render


class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        try:
            msg = self.request.GET['msg']
        except:
            msg = None

        if msg is None:
            msg = "Error getting the error, which tried to get the error [A cool example about recursivity]"

        template_values = {
            "title": "Error",
            "error_msg": msg,
            "content": "error"
        }

        render(self, template_values)

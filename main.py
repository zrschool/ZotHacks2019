import webapp2
import jinja2
import os

from google.appengine.ext import ndb
from google.appengine.api import users


jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class HousingOption(ndb.Model):
    name = ndb.StringProperty()
    rating = ndb.FloatProperty()
    description = ndb.StringProperty()





class MainPage(webapp2.RequestHandler):
    def get(self):


        template_vars = {
            # "var_name" : var_name,
        }

        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)

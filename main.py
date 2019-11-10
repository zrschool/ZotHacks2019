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


"""
    TODO:
    - Make add_housing_option function (see lines 31 through 44)
        - Take parameters: (name, rating, description="no description found")
"""


class MainPage(webapp2.RequestHandler):
    def get(self):

        # in terminal: dev_appserver app.yaml
        # in browser: localhost:8080 for websit, localhost:8000 for database

        # This creates an instance of the HousingOption model
        mesa_court_towers = HousingOption(
            name = "Mesa Court Towers",
            rating = 4.5,
            description = "Description TBA"
        )
        # This "puts" the model into the database, and saves the model's ID
        # so that we can use it later
        mesa_court_towers_key = mesa_court_towers.put()
        # This should print into our terminal so that we know this code ran
        print("NEW PROFILE ADDED")

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

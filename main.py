import webapp2
import jinja2
import os
import logging

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
        - Make key
"""

def make_housing_option(housing_name, average_rating, housing_description):
    '''
    Creates HousingOption Model
    '''
    return HousingOption(
        name = housing_name,
        rating = average_rating,
        description = housing_description
    )

def get_key_id(housing_option):
    '''
    Get model's id and puts the model into the database
    '''
    housing_option_key = housing_option.put()
    pair = housing_option_key.pairs()
    return (housing_option_key.urlsafe(), pair[0][1])


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
        mesa_court_towers_key = get_key_id(mesa_court_towers)
        # This should print into our terminal so that we know this code ran
        logging.info("NEW PROFILE ADDED")
        logging.info(mesa_court_towers_key)
        print("NEW PROFILE ADDED")
        print(mesa_court_towers_key)

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

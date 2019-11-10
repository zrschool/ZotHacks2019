import webapp2
import jinja2
import os
import logging
import housing
import reviews
import datetime
import sys
from google.appengine.ext import ndb
from google.appengine.api import users

sys.dont_write_bytecode = True
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class HousingOption(ndb.Model):
    name = ndb.StringProperty()
    rating = ndb.FloatProperty()
    location = ndb.StringProperty()
    photo = ndb.StringProperty()
    # description = ndb.StringProperty()

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
    return pair[0][1]    


class MainPage(webapp2.RequestHandler):
    

    def get(self):

        # Make a list of all housing options
        housing_options = HousingOption.query().order(HousingOption.name).order(-HousingOption.name)
        housing_options_keys = {}
        for item in housing_options:
            housing_options_keys[item.name] = get_key_id(item)

        print(housing_options_keys)


        template_vars = {
            "housing_options" : housing_options,
            "housing_options_keys" : housing_options_keys,
        }

        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))



class AddHousingOptionPage(webapp2.RequestHandler):
    def get(self):



        template_vars = {
            # "var_name" : var_name,
        }

        template = jinja_env.get_template("templates/add-housing-option.html")
        self.response.write(template.render(template_vars))


class HousingPage(webapp2.RequestHandler):
    def get(self):
        housing_id = self.request.get("id")
        housing_query = housing.housing_option_list()
        current_housing = HousingOption(
            name = "dsa",
            rating = 0.0
        )
        for option in housing_query:
            if housing.get_id(option) == int(housing_id):
                current_housing = option



        template_vars = {
            "current_housing" : current_housing,
            "housing_id" : housing_id,
        }

        template = jinja_env.get_template("templates/housing.html")
        self.response.write(template.render(template_vars))

    def post(self):
        pass

class UpdateDatabase(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        housing_option_name = str(self.request.get("option-name"))
        housing_option_rating = float(self.request.get("option-rating"))
        housing_option_location = str(self.request.get('option-location'))
        housing_option_photo = str(self.request.get('option-photo'))
        housing.create_housing_option(housing_option_name, housing_option_rating, housing_option_location, housing_option_photo)

        self.redirect("/")

class AboutPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {

        }
        template = jinja_env.get_template("templates/about-page.html")
        self.response.write(template.render(template_vars))


    def post(self):
        pass

class AddReview(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        user = users.get_current_user()
        user_review = str(self.request.get('housing-review'))
        user_rating = str(self.request.get('housing-rating'))
        current_time = datetime.datetime.now()
        housing = str(self.request.get('housing-name'))

        reviews.create_user_review(user, current_time, housing, user_review, user_rating)


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/add-housing-option", AddHousingOptionPage),
    ("/update-database", UpdateDatabase),
    ("/housing", HousingPage),
    ("/add-review", AddReview),
    ("/about-page", AboutPage)
], debug=True)

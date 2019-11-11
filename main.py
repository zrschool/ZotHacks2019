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
from reviews import UserReview

sys.dont_write_bytecode = True
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class HousingOption(ndb.Model):
    name = ndb.StringProperty()
    rating = ndb.FloatProperty()
    location = ndb.StringProperty()
    photo = ndb.StringProperty()
    reviews = ndb.KeyProperty(
        kind = UserReview,
        repeated = True,
    )

def find_housing_option(housing_id):
    """
    Gets a housing ID from the URL and returns the HousingOption model it is
    associated with. If no matching HousingOption model exists, returns string
    """
    all_housing_options = housing.housing_option_list()
    for option in all_housing_options:
        if housing.get_id(option) == int(housing_id):
            return option
    print("FIND HOUSING OPTION DID NOT WORK")



def make_housing_option(housing_name, average_rating, housing_description):
    '''
    Creates HousingOption Model
    '''
    return HousingOption(
        name = housing_name,
        rating = average_rating,
        description = housing_description
    )

def add_housing_review(user_review, housing_id):
    """
    Takes a UserReview model and appends it to the corresponding
    HousingOption model
    """

    current_housing = find_housing_option(housing_id).key.get()

    existing_reviews = current_housing.reviews
    new_review = [user_review]

    current_housing.reviews = existing_reviews + new_review
    print(current_housing.reviews)
    current_housing.put()
    print(current_housing.reviews)
    return current_housing






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
            name = "placeholder",
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
        housing_option_reviews = []
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
        current_time = datetime.datetime.now()
        housing_id = self.request.get("id")
        user_reviews = str(self.request.get('review-body'))
        user_rating = float(self.request.get('review-rating'))

        new_review = reviews.create_user_review(user, current_time, housing_id, user_reviews, user_rating)
        current_housing = find_housing_option(housing_id)
        current_housing = add_housing_review(new_review, housing_id)
        current_housing.put()

        self.redirect("/housing?id=" + housing_id)



app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/add-housing-option", AddHousingOptionPage),
    ("/update-database", UpdateDatabase),
    ("/housing", HousingPage),
    ("/add-review", AddReview),
    ("/about-page", AboutPage)
], debug=True)

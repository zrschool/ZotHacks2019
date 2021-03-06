import reviews
import sys

from google.appengine.ext import ndb
from reviews import UserReview


sys.dont_write_bytecode = True


class HousingOption(ndb.Model):
    name = ndb.StringProperty()
    rating = ndb.FloatProperty()
    location = ndb.StringProperty()
    photo = ndb.StringProperty()
    reviews = ndb.KeyProperty(
        kind = UserReview,
        repeated = True,
    )

def create_housing_option(option_name, option_rating, option_location, option_photo):
    new_option = HousingOption(
        name = option_name,
        rating = option_rating,
        location = option_location,
        photo = option_photo,
        reviews = []
        # description = description
    )
    print(new_option)
    new_option.put()

def calculate_average_rating(housing_option):
    total_rating_score = 0
    user_reviews = housing_option.reviews
    if len(user_reviews) != 0:
        for review in user_reviews:
            total_rating_score += review.rating
        housing_option.rating = total_rating_score / len(user_reviews)
    else:
        housing_option.rating = 0

    housing_option.put()

def housing_option_list():
    return list(HousingOption.query().fetch())

def housing_option_lex():
    return HousingOption.query().order(HousingOption.name)

def get_id(housing_option):
    housing_option_key = housing_option.put()
    pair = housing_option_key.pairs()
    return pair[0][1]
#
# def get_entry(housing_option_key):
#     return housing_option_key.get()
#
# def get_name(housing_option):
#     return housing_option.name
#
# def get_rating(housing_option):
#     return housing_option.rating
#
# def get_description(housing_option):
#     return housing_option.description

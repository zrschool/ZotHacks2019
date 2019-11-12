#reviews.py
import sys
from google.appengine.api import users
from google.appengine.ext import ndb
import housing
sys.dont_write_bytecode = True


class UserReview(ndb.Model):
    user =  ndb.UserProperty()
    date_time = ndb.DateTimeProperty()
    housing = ndb.IntegerProperty()
    review_body = ndb.StringProperty()
    rating = ndb.FloatProperty()

def get_key_id(housing_option):
    '''
    Get model's id and puts the model into the database
    '''
    housing_option_key = housing_option.put()
    pair = housing_option_key.pairs()
    return pair[0][1]

def get_key(user_review):
    '''
    Get model's id and puts the model into the database
    '''
    user_review_key = user_review.put()
    return user_review_key

def create_user_review(reviewing_user, submit_time, housing_id ,housing_review, housing_rating):
    """
    Creates instance of UserReview model and places it in database, then returns
    created model.
    """
    user_review = UserReview(
        user = reviewing_user,
        date_time = submit_time,
        housing = int(housing_id),
        review_body = housing_review,
        rating = housing_rating
    ).put()

    return user_review

def get_reviews(id):
    review_list = UserReview.query()
    return review_list.filter(UserReview.housing == int(id))

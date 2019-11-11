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
    review = ndb.StringProperty()
    rating = ndb.FloatProperty()

# def get_key(user_review):
#     '''
#     Get model's id and puts the model into the database
#     '''
#     user_review_key = user_review.put()
#     return user_review_key

def create_user_review(reviewing_user, submit_time, housing_id ,housing_review, housing_rating):
    # housing_query = housing.housing_option_list()
    # current_housing = None
    # for option in housing_query:
    #     if housing.get_id(option) == int(housing_id):
    #         current_housing = option
    
    user_review = UserReview(
        user = reviewing_user,
        date_time = submit_time,
        housing = int(housing_id),
        review = housing_review,
        rating = housing_rating
    )
    # current_housing.user_reviews.append(get_key(user_review))
    # current_housing.put()
    user_review.put()
    
def get_reviews(id):
    review_list = UserReview.query()
    return review_list.filter(UserReview.housing == int(id))



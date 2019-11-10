#reviews.py
import sys
from google.appengine.api import users
from google.appengine.ext import ndb
sys.dont_write_bytecode = True
class UserReview(ndb.Model):
    user =  ndb.UserProperty()
    date_time = ndb.DateTimeProperty()
    housing = ndb.StringProperty()
    review = ndb.StringProperty()
    rating = ndb.FloatProperty()

def create_user_review(reviewing_user, submit_time, housing_name ,housing_review, housing_rating):
    user_review = UserReview(
        user = reviewing_user,
        date_time = submit_time,
        housing = housing_name,
        review = housing_review,
        rating = housing_rating
    )
    user_review.put()

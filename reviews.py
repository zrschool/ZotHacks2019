#reviews.py

from google.appengine.api import users
from google.appengine.ext import ndb

class UserReview(ndb.Model):
    user =  ndb.UserProperty()
    review = ndb.StringProperty()
    rating = ndb.FloatProperty()

def create_user_review(reviewing_user, housing_review, housing_rating):
    user_review = UserReview(
        user = reviewing_user,
        review = housing_review,
        rating = housing_rating
    )
    return user_review.put()

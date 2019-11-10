#reviews.py

from google.appengine.api import users
from google.appengine.ext import ndb

class UserReview(ndb.model):
    user =  ndb.UserProperty()
    review = ndb.StringProperty()
    ratings = ndb.FloatProperty()
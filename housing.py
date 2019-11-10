from google.appengine.ext import ndb

class HousingOption(ndb.Model):
    housing_name = ndb.StringProperty()
    rating = ndb.FloatProperty()
    description = ndb.StringProperty()

def create_housing_option(name, rating, description):
    new_option = HousingOption(
        name = name,
        rating = rating,
        description = description
    )
    new_option.put()
    return new_option.key()

def get_id(housing_option_key):
    pair = housing_option_key.pairs()
    return (housing_option_key.urlsafe(), pair[0][1])

def get_entry(housing_option_key):
    return housing_option_key.get()

def get_name(housing_option):
    return housing_option.key.name

def get_rating(housing_option):
    return housing_option.key.rating

def get_description(housing_option):
    return housing_option.key.description
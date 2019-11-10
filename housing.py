from google.appengine.ext import ndb

class HousingOption(ndb.Model):
    name = ndb.StringProperty()
    rating = ndb.FloatProperty()
    location = ndb.StringProperty()
    # description = ndb.StringProperty()

def create_housing_option(option_name, option_rating, option_location):
    new_option = HousingOption(
        name = option_name,
        rating = option_rating,
        location = option_location
        # description = description
    )
    new_option.put()
    # return new_option.key()

# def get_id(housing_option_key):
#     pair = housing_option_key.pairs()
#     return (housing_option_key.urlsafe(), pair[0][1])
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

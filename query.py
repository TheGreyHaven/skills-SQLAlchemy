"""

This file is the place to write solutions for the
practice part of skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes by just their
class name (and not model.ClassName).

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = db.session.query(Brand).filter(Brand.brand_id == 'ram').first()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter((Model.name == 'Corvette') & (Model.brand_id == 'che')).all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('%Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued == None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Brand.query.filter(Brand.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 3: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    
    car_information = db.session.query(Model, Brand).outerjoin(Brand).all()

    for mod, bran in car_information:
        if mod.year == year:
            print "%s, %s, %s" % (mod.name, bran.name, bran.headquarters)


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    info_by_brand = db.session.query(Model, Brand).outerjoin(Brand).order_by(Brand.name).all()

    
    for mod, bran in info_by_brand:
        if mod.brand_id == bran.brand_id:
            print bran.name, mod.name, mod.year



def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""
    

    brand_obj = db.session.query(Brand).all()

    for bran in brand_obj:
        if mystr in bran.name:
            print bran.name
    


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""


    model_obj = db.session.query(Model).all()

    for mod in model_obj:
        if mod.year >= start_year and mod.year < end_year:
            print mod.name


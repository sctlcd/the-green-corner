import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import send_from_directory
from os import path
if path.exists('env.py'):
    import env

# app initialization + configuration
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'the_green_corner'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# reusable extension for PyMongo
mongo = PyMongo(app)



@app.route('/favicon.ico')
def favicon():
    """
        Get the browsers to find my favicon.
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# ---------------------- #
#    APP ROUTES - HOME   #
# ---------------------- #

@app.route('/')
@app.route('/home')
def get_home():
    """
        Home page to introduce the application.

        Display the application purposes, contact and support the project, with option to Search.
    """
    return render_template("home.html")


# ------------------------ #
#    APP ROUTES - PLANTS   #
# ------------------------ #

# ------------------------------------------- #
#    CRUD: Create | Read | Update | Delete    #
# ------------------------------------------- #

# ------------------------------------ READ ----- #
@app.route('/get_plants')
def get_plants():
    """
        Read all plants from database.

        Display all plants initially, with option to Search.
    """
    return render_template("plants.html", plants=mongo.db.plants.find())


# ------------------------------------ CREATE ----- #
@app.route('/add_plant')
def add_plant():
    """
        Create plant for database.

        Inject all form data to new plant document on submit.
    """
    all_plant_types =  mongo.db.plant_types.find()
    all_plants = mongo.db.plants.find()
    all_shade_tolerance = mongo.db.shade_tolerance.find()
    return render_template('addplant.html',
                           plant_types=all_plant_types,
                           plants=all_plants,
                           shade_tolerance=all_shade_tolerance)


@app.route('/insert_plant', methods=['POST'])
def insert_plant():
    """
        Insert new plant document into the database.
    """
    plants = mongo.db.plants
    plants.insert_one(request.form.to_dict())
    return redirect(url_for('get_plants'))


# ------------------------------------ UPDATE ----- #
@app.route('/edit_plant/<plant_id>')
def edit_plant(plant_id):
    """
        Edit plant for database.

        Inject all existing data from the plant document into the form.
    """
    the_plant =  mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    all_plant_types =  mongo.db.plant_types.find()
    all_shade_tolerance = mongo.db.shade_tolerance.find()
    return render_template('editplant.html',
                            plant=the_plant,
                            plant_types=all_plant_types,
                            shade_tolerance=all_shade_tolerance)


@app.route('/update_plant/<plant_id>', methods=["POST"])
def update_plant(plant_id):
    """
        Push the edits of the plant form to the Plants collection on submit.
    """
    plants = mongo.db.plants
    plants.update( {'_id': ObjectId(plant_id)},
    {
        'scientific_name':request.form.get('scientific_name'),
        'common_name':request.form.get('common_name'),
        'genus': request.form.get('genus'),
        'species': request.form.get('species'),
        'family':request.form.get('family'),
        'plant_type':request.form.get('plant_type'),
        'shade_tolerance':request.form.get('shade_tolerance'),
        'note':request.form.get('note')
    })
    return redirect(url_for('get_plants'))


# ------------------------------------ DELETE ----- #
@app.route('/delete_plant/<plant_id>')
def delete_plant(plant_id):
    """
        Delete plant from database.

        Remove the plant document from the Plants collection.
    """
    mongo.db.plants.remove({'_id': ObjectId(plant_id)})
    return redirect(url_for('get_plants'))


# ------------------------------------ SEARCH ----- #
@app.route('/search_plants', methods=['POST'])
def search_plants():
    """
        Search plant by common name from database.

        Display all the database records matching with the search text entered.
    """
    search_text = request.form.get('search_text')
    plants_search = list(mongo.db.plants.find({'common_name': {"$regex": f'.*{search_text}.*'}}))
    return render_template("plantresults.html", plants_search=plants_search)


# ---------------------------- #
#    APP ROUTES - CATEGORIES   #
# ---------------------------- #

# ------------------------------------------- #
#    CRUD: Create | Read | Update | Delete    #
# ------------------------------------------- #

# ------------------------------------ READ ----- #
@app.route('/get_categories')
def get_categories():
    """
        Read all categories from database.

        Display all categories initially.
    """
    all_categories = mongo.db.categories.find()
    all_plant_types = mongo.db.plant_types.find()
    all_shade_tolerance = mongo.db.shade_tolerance.find()
    return render_template("categories.html",
                            categories=all_categories,
                            plant_types=all_plant_types,
                            shade_tolerance=all_shade_tolerance)


# ------------------------------------ CREATE ----- #
@app.route('/add_category')
def add_category():
    """
        Create category for database.

        Inject all form data to new category document on submit.
    """
    all_plant_types = mongo.db.plant_types.find()
    all_shade_tolerance = mongo.db.shade_tolerance.find()
    return render_template('addcategory.html',
                           plant_types=all_plant_types,
                           shade_tolerance=all_shade_tolerance)


@app.route('/insert_category', methods=['POST'])
def insert_category():
    """
        Insert new category document into the database.
    """
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('get_categories'))


# ------------------------------------ UPDATE ----- #
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    """
        Edit category for database.

        Inject all existing data from the category document into the form.
    """
    the_category =  mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template('editcategory.html',
                            category=the_category)


@app.route('/update_category/<category_id>', methods=["POST"])
def update_category(category_id):
    """
        Push the edits of the category form to the Categories collection on submit.
    """
    categories = mongo.db.categories
    categories.update( {'_id': ObjectId(category_id)},
    {
        'category_name':request.form.get('category_name'),
    })
    return redirect(url_for('get_categories'))


# ------------------------------------ DELETE ----- #
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    """
        Delete category from database.

        Remove the category document from the Categories collection.
    """
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists('env.py'):
    import env


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'the_green_corner'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def get_home():
    return render_template("home.html")


# ------------------------------------------------ Plants --------------------------------------------------

@app.route('/get_plants')
def get_plants():
    return render_template("plants.html", plants=mongo.db.plants.find())


@app.route('/add_plant')
def add_plant():
    all_plant_types =  mongo.db.plant_types.find()
    all_plants = mongo.db.plants.find()
    all_shade_tolerance = mongo.db.shade_tolerance.find()
    return render_template('addplant.html',
                           plant_types=all_plant_types,
                           plants=all_plants,
                           shade_tolerance=all_shade_tolerance)


@app.route('/insert_plant', methods=['POST'])
def insert_plant():
    plants = mongo.db.plants
    plants.insert_one(request.form.to_dict())
    return redirect(url_for('get_plants'))


@app.route('/edit_plant/<plant_id>')
def edit_plant(plant_id):
    the_plant =  mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    all_plant_types =  mongo.db.plant_types.find()
    all_shade_tolerance = mongo.db.shade_tolerance.find()
    return render_template('editplant.html',
                            plant=the_plant,
                            plant_types=all_plant_types,
                            shade_tolerance=all_shade_tolerance)


@app.route('/update_plant/<plant_id>', methods=["POST"])
def update_plant(plant_id):
    plants = mongo.db.plants
    plants.update( {'_id': ObjectId(plant_id)},
    {
        'scientific_name':request.form.get('scientific_name'),
        'common_name':request.form.get('common_name'),
        'genus': request.form.get('genus'),
        'species': request.form.get('species'),
        'family':request.form.get('family'),
        'plant_type':request.form.get('plant_type')
    })
    return redirect(url_for('get_plants'))


@app.route('/delete_plant/<plant_id>')
def delete_plant(plant_id):
    mongo.db.plants.remove({'_id': ObjectId(plant_id)})
    return redirect(url_for('get_plants'))


# ------------------------------------------------ Categories --------------------------------------------------

@app.route('/get_categories')
def get_categories():
    all_categories = mongo.db.categories.find()
    all_plant_types = mongo.db.plant_types.find()
    all_shade_tolerance = mongo.db.shade_tolerance.find()
    return render_template("categories.html",
                            categories=all_categories,
                            plant_types=all_plant_types,
                            shade_tolerance=all_shade_tolerance)


@app.route('/add_category')
def add_category():
    all_plant_types = mongo.db.plant_types.find()
    all_shade_tolerance = mongo.db.shade_tolerance.find()
    return render_template('addcategory.html',
                           plant_types=all_plant_types,
                           shade_tolerance=all_shade_tolerance)


@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    the_category =  mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template('editcategory.html',
                            category=the_category)


@app.route('/update_category/<category_id>', methods=["POST"])
def update_category(category_id):
    categories = mongo.db.categories
    categories.update( {'_id': ObjectId(category_id)},
    {
        'category_name':request.form.get('category_name'),
    })
    return redirect(url_for('get_categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

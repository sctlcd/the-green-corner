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
    return render_template('addplant.html',
                           plant_types=mongo.db.plant_types.find(), plants=mongo.db.plants.find())


@app.route('/insert_plant', methods=['POST'])
def insert_plant():
    plants = mongo.db.plants
    plants.insert_one(request.form.to_dict())
    return redirect(url_for('get_plants'))


@app.route('/edit_plant/<plant_id>')
def edit_plant(plant_id):
    the_plant =  mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    all_plant_types =  mongo.db.plant_types.find()
    return render_template('editplant.html', plant=the_plant,
                           plant_types=all_plant_types)


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
    return render_template("categories.html", categories=mongo.db.categories.find(),
            plant_types=mongo.db.plant_types.find(), shade_tolerance=mongo.db.shade_tolerance.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

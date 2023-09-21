#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return '<h1>Zoo app</h1>'


@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)

    if animal:

        animal_data = {
            'id': animal.id,
            'name': animal.name,
            'species': animal.species,
            'zookeeper_id': animal.zookeeper_id,
            'enclosure_id': animal.enclosure_id
        }
        return make_response(animal_data, 200)
    else:
        return make_response({'message': 'Animal not found'}, 404)


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)

    if zookeeper:

        zookeeper_data = {
            'id': zookeeper.id,
            'name': zookeeper.name,
            'birthday': zookeeper.birthday,
            'animals': [{'id': animal.id, 'name': animal.name} for animal in zookeeper.animals]
        }
        return make_response(zookeeper_data, 200)
    else:
        return make_response({'message': 'Zookeeper not found'}, 404)


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)

    if enclosure:

        enclosure_data = {
            'id': enclosure.id,
            'environment': enclosure.environment,
            'open_to_visitors': enclosure.open_to_visitors,
            'animals': [{'id': animal.id, 'name': animal.name} for animal in enclosure.animals]
        }
        return make_response(enclosure_data, 200)
    else:
        return make_response({'message': 'Enclosure not found'}, 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

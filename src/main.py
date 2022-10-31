"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import db, Character
from models import db, Planet
from models import db, favorite
from models import db, type_item

from datetime import timedelta


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/api/hello', methods=['GET'])
def handle_hello():
    response_body = {
        "msg": "Hello, don pepito "
    }
    return jsonify(response_body), 200


@app.route('/character', methods=['GET'])
def get_all_character():
    all_character = Character.query.all()
    character_list = list(map(lambda obj: obj.serialize(), all_character))
    print(character_list)
    response_body = {
        "success": True,
        "result": character_list
    }

    return jsonify(response_body), 200


@app.route('/api/character', methods=['POST'])
def add_character():
    body = request.get_json()
    new_character = Character(name=body["name"], status=body["status"], species=body["species"], type_character=body["type_character"], gender=body["gender"],
                              origin=body["origin"], location=body["location"], image=body["image"], episode=body["episode"], url=body["url"], created=body["created"])
    db.session.add(new_character)
    db.session.commit()
    print(new_character)
    response_body = {
        "success": True,
        "result": character_list
    }

    return jsonify(response_body), 200


@app.route('/api/character/<int:idCharacter>', methods=['GET'])
def get_character_by_id(idCharacter):
    characterByid = Character.query.filter_by(id=idCharacter).first()
    print(characterByid)
    character_by_id = characterByid.serialize()
    response_body = {
        "success": True,
        "result": character_by_id
    }

    return jsonify(response_body), 200


@app.route('/api/planet', methods=['GET'])
def get_all_planet():
    all_planet = Planet.query.all()
    planet_list = list(map(lambda obj: obj.serialize(), all_planet))
    print(planet_list)
    response_body = {
        "success": True,
        "result": planet_list
    }

    return jsonify(response_body), 200


@app.route('/api/planet/<int:idPlanet>', methods=['GET'])
def get_planet_by_id(idPlanet):
    planetByid = Planet.query.filter_by(id=idPlanet).first()
    print(planetByid)
    planet_by_id = planetByid.serialize()
    response_body = {
        "success": True,
        "result": planet_by_id
    }

    return jsonify(response_body), 200


@app.route('/api/user', methods=['GET'])
def get_all_user():
    all_user = User.query.all()
    user_list = list(map(lambda obj: obj.serialize(), all_user))
    print(user_list)
    response_body = {
        "success": True,
        "result": user_list
    }

    return jsonify(response_body), 200


@app.route('/api/user/<int:idUser>', methods=['GET'])
def get_user_by_id(idUser):
    UserByid = User.query.filter_by(id=idUser).first()
    print(UserByid)
    user_by_id = UserByid.serialize()
    response_body = {
        "success": True,
        "result": user_by_id
    }

    return jsonify(response_body), 200


@app.route('/api/favorite/<int:idUser>', methods=['GET'])
def get_favorite_by_user(idUser):
    list_favorites = []
    list_favorites_by_user = db.session.query(
        favorite).filter(favorite.fk_user == idUser).all()
    list_type_item = db.session.query(type_item).all()
    for favorite_by_user in list_favorites_by_user:
        if favorite_by_user.type_item == list_type_item[0]:
            character_favorite = db.session.query(Character).filter(
                Character.id == favorite.fk_id_item).first()
            list_favorites.append({
                'Name': character_favorite.name,
                'idItem': character_favorite.id
            })
        if favorite_by_user.type_item == list_type_item[1]:
            planet_favorite = db.session.query(Planet).filter(
                Planet.id == favorite.fk_id_item).first()
            list_favorites.append({
                'Name': planet_favorite.name,
                'idItem': planet_favorite.id
            })
    print(list_favorites)
    response_body = {
        "success": True,
        "result": list_favorites
    }

    return jsonify(response_body), 200


@app.route('/api/favorite/<int:idUser>', methods=['POST'])
def post_favorite_by_user(idUser):
    body = request.get_json()
    new_favorite = favorite(
        fk_id_item=body["id"], fk_user=idUser, fk_id_type_item=body["fk_type_item"])
    db.session.add(new_favorite)
    db.session.commit()

    response_body = {
        "success": True,
        "result": 'Favorite created'
    }

    return jsonify(response_body), 200


@app.route('/api/favorite/<int:idUser>/<int:idItem>', methods=['DELETE'])
def delete_favorite_by_user(idUser, idItem):
    delete_favorite = db.session.query(
        favorite).filter(favorite.id == idItem).first()

    db.session.delete(delete_favorite)
    db.session.commit()

    response_body = {
        "success": True,
        "result": 'Favorite deleted'
    }

    return jsonify(response_body), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

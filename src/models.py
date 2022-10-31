from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    favorite = db.relationship(
        'favorite', backref='User', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)
    species = db.Column(db.String(80), unique=False, nullable=False)
    type_character = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    origin = db.Column(db.String(80), unique=False, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    image = db.Column(db.String(80), unique=False, nullable=False)
    episode = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
    fk_type_item = db.Column(
        db.Integer, db.ForeignKey('type_item.id'))

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "type_character": self.type_character,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "image": self.image,
            "episode": self.episode,
            "url": self.url,
            "created": self.created,
            "fk_type_item": self.fk_type_item
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=True)
    image = db.Column(db.String(200), unique=False, nullable=True)
    fk_type_item = db.Column(
        db.Integer, db.ForeignKey('type_item.id'))

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "image": self.image,
            "fk_type_item": self.fk_type_item
        }


class favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    fk_id_type_item = db.Column(
        db.Integer, db.ForeignKey('type_item.id'))
    fk_id_item = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "fk_user": self.fk_user,
            "fk_id_type_item": self.fk_id_type_item,
            "fk_id_item": self.fk_id_item,
        }


class type_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_type_item = db.Column(db.String(120), unique=True, nullable=False)
    favorite = db.relationship(
        'favorite', backref='type_item', lazy=True)
    favorite_character = db.relationship(
        'Character', backref='type_item', lazy=True)
    favorite_planet = db.relationship(
        'Planet', backref='type_item', lazy=True)

    def __repr__(self):
        return '<type_item %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name_type_item": self.name_type_item
        }

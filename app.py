# Marshmallow nos permite deserializar objetos de una base de datos. Es decir, nos permite trabajar con cada objeto. 

import os
from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt
)


from werkzeug.security import (check_password_hash, generate_password_hash) 

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=False, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
  
class UserBasicSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    
    funcion = fields.Function() # Va a retornar una función.
    saludo_user = fields.Method('probando_metodo') # Obtiene un campo a través de un método.

    def probando_metodo(self, obj):
        return f"Bienvenido: {obj.username}"

class UserAdminSchema(UserBasicSchema): # Siempre usar el subfijo Schema porque facilita su trabajo. Ej: UserAdminSchema o UserBasicSchema.
    id = fields.Integer(dump_only=True)
    username = fields.String()
    password = fields.String()
    
@app.route('/add_user', methods = ['POST'])
def addUser():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    password_hash = generate_password_hash( # Genera una contraseña hasheada, es decir, encriptada.
        password = password, method="pbkdf2", salt_length=16
        )
    
    newUser = User(username = username, password = password_hash)
    db.session.add(newUser)
    db.session.commit()

    return jsonify({'OK': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=user).first() # Retorna una lista si encuentra el usuario filtrado por nombre de usuario. En caso de no encontrarlo, devuelve una lista vacía.

    if user and check_password_hash(
        user.password, password # Compara la contraseña de la base de datos y la del formulario (introducida por el usuario).
    ):
        access_token = create_access_token(
            identity=user.username,
            expires_delta=timedelta(seconds=30),
            additional_claims={'id_user': user.id} 
        )
        return {
            "OK":"Usuario Logeado",
            "Token":access_token
            }
    
    return {"Error": "El usuario no se encontro"}

@app.route('/restringida')
@jwt_required()
def restringida():
    return {"Ok":"EL usuario puede entrar"}

def suma(a: int, b: int)-> int:
    return a+b

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users') # Nos va a generar una lista de diccionarios.
def get_all_users():
    users = User.query.all()
    users_schema = UserBasicSchema().dump(users, many = True) # el parámetro "many" indica si le vamos a pasar más de un objeto o no (True = varios objetos, False = un solo objeto)
    return jsonify(users_schema)
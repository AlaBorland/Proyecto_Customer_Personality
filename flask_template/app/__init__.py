from flask import Flask
from flask_cors import CORS
from app.routes.model.controller import customer_blueprint
from dotenv import dotenv_values,load_dotenv
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)

#----------declarar variable de entorno----------
ENV = dotenv_values(".env")
load_dotenv(override=False)
print("Env: ",ENV)
#-------------------------------------------------
CORS(app)
#CORS(app,supports_credentials=True)
#app.config["JWT_SECRET_KEY"] = os.environ['JWT_KEY']# Change this "super secret" with something else!
#jwt = JWTManager(app)
app.register_blueprint(customer_blueprint)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "API is  up and running"
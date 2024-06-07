from flask import Flask
from flasgger import Swagger
from src.config.config import Config
from src.routes import api

app = Flask(__name__)
swagger = Swagger(app)

config = Config().dev

app.env = config.ENV

app.register_blueprint(api, url_prefix='/api')

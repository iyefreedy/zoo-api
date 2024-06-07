from flask import Blueprint
from src.controllers.animal_controller import animals_blueprint
from src.controllers.employee_controller import employee_blueprint

api = Blueprint('api', __name__)

api.register_blueprint(animals_blueprint, url_prefix='/animals')
api.register_blueprint(employee_blueprint, url_prefix='/employees')

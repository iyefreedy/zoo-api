from flask import Blueprint
from src.controllers.animal_controller import animals_blueprint
from src.controllers.employee_controller import employee_blueprint
from src.controllers.feeding_controller import feeding_blueprint
from src.controllers.enclosure_controller import enclosure_blueprint
from src.controllers.report_controller import report_blueprint

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(animals_blueprint)
api.register_blueprint(employee_blueprint)
api.register_blueprint(feeding_blueprint)
api.register_blueprint(enclosure_blueprint)
api.register_blueprint(report_blueprint)

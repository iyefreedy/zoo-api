from flask import Blueprint, jsonify
from flasgger import swag_from
from src.repositories.animal_repository import AnimalRepository
from src.repositories.visitor_repository import VisitorRepository
from src.repositories.revenue_repository import RevenueRepository

animal_repo = AnimalRepository()
visitor_repo = VisitorRepository()
revenue_repo = RevenueRepository()

report_blueprint = Blueprint('reports', __name__, url_prefix='/reports')


@report_blueprint.get('/animals')
@swag_from('../docs/report/get_animal_report.yml')
def get_animal_report():
    animal_report = animal_repo.get_all()
    return jsonify({"data": animal_report})


@report_blueprint.get('/visitors')
@swag_from('../docs/report/get_visitor_report.yml')
def get_visitor_report():
    return jsonify({"data": visitor_repo.get_all()})


@report_blueprint.get('/revenue')
@swag_from('../docs/report/get_revenue_report.yml')
def get_revenue_report():
    return jsonify({"data": revenue_repo.get_all()})

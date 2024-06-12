from flask import Flask
from werkzeug.exceptions import HTTPException
from src import database
from src.controllers.data_controller import DataController

def create_app(db_uri:str):
    app = Flask(__name__)
    database.get_client(db_uri)
    registerAPIRoutes(app)
    return app

def registerAPIRoutes(appIn):
    appIn.add_url_rule("/", methods=["GET"], view_func=DataController.root)
    appIn.add_url_rule('/data', methods=['POST'], view_func=DataController.create_data_endpt)
    appIn.add_url_rule('/data/<id>', methods=['GET'], view_func=DataController.get_data_endpt)
    appIn.add_url_rule('/data/<id>', methods=['PUT'], view_func=DataController.update_data_endpt)
    appIn.add_url_rule('/data/<id>', methods=['DELETE'], view_func=DataController.delete_data_endpt)
    appIn.register_error_handler(HTTPException, DataController.handle_exception)
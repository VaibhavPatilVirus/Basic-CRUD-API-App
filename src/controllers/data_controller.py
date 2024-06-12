from flask import request, jsonify
#from pymongo.errors import PyMongoError, ConnectionFailure, OperationFailure
from bson.objectid import ObjectId
from src import database

class DataController:

    @staticmethod
    def create_data(collection, data):
        clnt = database.get_client()
        #collection.database.client
        #try:
            # with clnt.start_session() as session:
            #     with session.start_transaction():
        result = collection.insert_one(data)
                    # session.commit_transaction()
        return result
        # except ConnectionFailure as cf:
        #     return f"Connection to MongoDB failed: {cf}"
        # except OperationFailure as of:
        #     return f"Operation failed: {of}"
        # except PyMongoError as pme:
        #     return f"An error occurred with PyMongo: {pme}"
        # except Exception as e:
        #     session.abort_transaction()
        #     return f"An unexpected error occurred: {e}"
        #finally:
        #    session.end_session()

    @staticmethod
    def root():
        try:
            return jsonify({"error":"Not a valid API endpoint."}), 405
        except Exception as e:
            return jsonify({"error":"Internal server error."}), 500



    @staticmethod
    def create_data_endpt():
        try:
            data = request.get_json(silent=True)
            if not data:
                return jsonify({"error":"Invalid Data Format."}), 400
            result = DataController.create_data(database.get_collection("CRUDApp", "data"), data)
            return jsonify({"id": str(result.inserted_id)}), 201
        except Exception as e:
            return jsonify({"error":"Internal server error."}), 500

    @staticmethod
    def get_data_endpt(id):
        try:
            if not ObjectId.is_valid(id):
                return jsonify({"error": "Invalid data ID."}), 400
            data = database.get_collection("CRUDApp", "data").find_one({"_id": ObjectId(id)})
            if not data:
                return jsonify({"error": "Data not found"}), 404
            dataCopy = data.copy()
            dataCopy['_id'] = str(dataCopy['_id'])
            return jsonify(dict(dataCopy)), 200
        except Exception as e:
            return jsonify({"error":"Internal server error."}), 500

    @staticmethod
    def update_data_endpt(id):
        try:
            if not ObjectId.is_valid(id):
                return jsonify({"error": "Invalid data ID."}), 400
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid JSON"}), 400
            result = database.get_collection("CRUDApp", "data").update_one({"_id": ObjectId(id)}, {"$set": data})
            if result.matched_count == 0:
                return jsonify({"error": "Data not found"}), 404
            return jsonify({"message": "Data updated"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_data_endpt(id):
        try:
            if not ObjectId.is_valid(id):
                return jsonify({"error": "Invalid data ID."}), 400
            result = database.get_collection("CRUDApp", "data").delete_one({"_id": ObjectId(id)})
            if result.deleted_count == 0:
                return jsonify({"error": "Data not found"}), 404
            return jsonify({"message": "Data deleted"}), 200
        except Exception as e:
            return jsonify({"error":"Internal server error."}), 500

    @staticmethod
    def handle_exception(e):
        return jsonify({"error":"Internal server error."}), e.code
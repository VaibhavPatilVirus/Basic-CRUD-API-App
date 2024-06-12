from src import app

if __name__=="__main__":
    db_uri = "mongodb://'127.0.0.1:27017/mydatabase"
    flaskApp = app.create_app()
    flaskApp.run("0.0.0.0", port=5000, debug=False)
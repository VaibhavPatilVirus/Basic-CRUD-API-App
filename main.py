from src import app

if __name__=="__main__":
    db_uri = "mongodb://localhost:27017/"
    flaskApp = app.create_app(db_uri)
    flaskApp.run("0.0.0.0", port=5000, debug=False)
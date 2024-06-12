from src import app
import os

if __name__=="__main__":
    db_uri = os.getenv('DATABASE_URL')
    app_port = os.getenv('APP_PORT')
    flaskApp = app.create_app(db_uri)
    flaskApp.run("0.0.0.0", port=app_port, debug=False)
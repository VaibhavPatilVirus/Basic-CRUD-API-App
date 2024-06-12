from src import app
import os

#Start the server.
if __name__=="__main__":
    db_uri = os.getenv('DATABASE_URL')
    app_port = os.getenv('APP_PORT')
    host = os.getenv('APP_HOST')
    flaskApp = app.create_app(db_uri)
    flaskApp.run(host, port=app_port, debug=False)
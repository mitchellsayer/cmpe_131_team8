from app import *

''' 
    Only use run.py when running app in development mode.

    Alternativeley, run the app with the following commands:
        1. export FLASK_APP=app
        2. export FLASK_ENV=development
        3. python3 -m flask run
'''

if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(debug=True)

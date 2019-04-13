from flask import Flask

# create_app wraps the other functions to set up the project

def create_app(config=None, testing=False, cli=True):
    """
    Application factory, used to create application
    """
    app = Flask(__name__, static_folder=None)

    @app.route("/")
    def hello():
        return "Hello World!"

    return app

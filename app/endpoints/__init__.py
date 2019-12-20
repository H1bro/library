

from .library import books_blueprint

def register_blueprints_books(app):
    app.register_blueprint(books_blueprint)

#####################################################

from .library import litterateurs_blueprint

def register_blueprints_litterateurs(app):
    app.register_blueprint(litterateurs_blueprint)

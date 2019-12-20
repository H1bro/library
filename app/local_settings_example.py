import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = 'This is an UNSECURE Secret. CHANGE THIS for production environments.'

# SQLAlchemy settings
DATABASE_FILE_PATH = os.path.join(os.getcwd(), "app.sqlite")
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % DATABASE_FILE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning

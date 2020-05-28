import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODONE IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://rishabhgajra@localhost:5432/Fyyur'
from BookModel import *
from flask_sqlalchemy import SQLAlchemy
from settings import *
import json
Book.add_book("Lagaan", 8.66, 789645223)
Book.get_all_books()
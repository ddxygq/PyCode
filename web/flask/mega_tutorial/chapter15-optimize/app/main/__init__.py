from flask import Blueprint

bp = Blueprint('main', __name__)

import sys
sys.path.append('../..')

from app.main import routes
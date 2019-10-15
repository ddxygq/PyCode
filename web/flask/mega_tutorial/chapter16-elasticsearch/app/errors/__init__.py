from flask import Blueprint

bp = Blueprint('error', __name__)

import sys
sys.path.append('../..')

from app.errors import handlers
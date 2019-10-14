from flask import Blueprint
import sys
sys.path.append('../..')

bp = Blueprint('auth', __name__)

from app.auth import routes
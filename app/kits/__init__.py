from flask import Blueprint

bp = Blueprint('kits', __name__, url_prefix='/kits')

from . import views

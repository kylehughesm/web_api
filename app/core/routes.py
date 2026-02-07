
from flask import Blueprint

core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def index(): 
    return "200 OK Succesful!", 200
    

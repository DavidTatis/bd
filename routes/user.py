from flask import Blueprint, request
users = Blueprint('users', __name__)

@users.route("/", methods=('GET', 'POST'))
def index_page():
    if request.method == 'POST':
        return "This is a  POST burritos"+str(request.json)
    else:
        return "This is a GET burritos"

@users.route("/about")
def about_page():
  return "This is a website about burritos"
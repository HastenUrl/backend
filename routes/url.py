from flask import Blueprint

url_route = Blueprint('url_route', __name__)

@url_route.route('/url-details')
def url_details():
    return {"message": "success"}
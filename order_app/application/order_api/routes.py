from flask import jsonify, request, make_response
from . import order_api_blueprint
from .. import db
from ..models import Order, OrderItem
from .api.user_client import UserClient


@order_api_blueprint.route("/api/orders", methods=["GET"])
def orders():
    items = []
    for row in Order.query.all():
        items.append(row.to_json())

    response = jsonify(items)
    return response


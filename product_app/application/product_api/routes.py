
from .. import db
from ..models import Product
from flask import jsonify, request

from . import product_api_blueprint


@product_api_blueprint.route("/api/products", methods=["GET"])
def product():
    items = []
    for row in Product.query.all():
        items.append(row.to_json())

    response = jsonify({"result": items})
    return response


@product_api_blueprint.route("/api/product/create", methods=["POST"])
def post_create():
    name = request.form["name"]
    slug = request.form["slug"]
    image = request.form["image"]
    price = request.form["price"]

    item = Product(name=name, slug=slug, image=image, price=price)

    db.session.add(item)
    db.session.commit()

    response = jsonify({"message": "Product add", "product": item.to_json()})

    return response


@product_api_blueprint.route("/api/product/<slug>", methods=["GET"])
def product_slug(slug):
    item = Product.query.filter_by(slug=slug).first()
    if item is not None:
        response = jsonify({"result": item.to_json()})
    else:
        response = jsonify({"message": "cannot find product"}), 404

    return response

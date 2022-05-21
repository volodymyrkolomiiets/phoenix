from . import db
from datetime import datetime


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    items = db.relationship('OrderItem', backref='order_item')
    is_open = db.Column(db.Boolean, default=True)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def create(self, user_id):
        self.user_id = user_id
        self.is_open = True
        return self

    def to_json(self):
        items = []
        for i in self.items:
            items.append(i.to_json())

        return {
            "items": items,
            "is_open": self.is_open,
            "user_id": self.user_id
        }


class OrderItem(db.Model):
    __tablename__ = "order_item"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer, default=1)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

    def to_json(self):
        return {
            "product": self.product_id,
            "quantity": self.quantity
        }

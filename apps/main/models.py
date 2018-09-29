import datetime

from apps.ext import db


class User(db.Model):
    # name 表示列名
    # 修改表名
    # __tablename__ = ''
    user_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    is_delete = db.Column(db.Boolean, default=False)
    # wight = db.Column(db.Float(2))
    price = db.Column(db.Numeric(7, 2), nullable=False)

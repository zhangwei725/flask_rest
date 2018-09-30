import datetime

from apps.ext import db


class Navigation(db.Model):
    nav_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nav_name = db.Column(db.String(64), index=True, unique=True, nullable=False)


class Banner(db.Model):
    banner_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), index=True, unique=True, nullable=False)
    image = db.Column(db.String(64))
    detail_url = db.Column(db.String(64))
    order = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


class Category(db.Model):
    cate_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)

# 路由系统
from flask_restful import Api

from apps.main.apis import IndexApi

api = Api()


def init_api(app):
    api.init_app(app)


# 注册路由系统
api.add_resource(IndexApi, '/')

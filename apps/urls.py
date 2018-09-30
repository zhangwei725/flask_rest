# 路由系统
from flask_restful import Api

from apps.home.apis import HomeHeadApi, HomeDataApi
from apps.main.apis import IndexApi

api = Api(prefix='/api/v1')


def init_api(app):
    api.init_app(app)


# 注册路由系统
api.add_resource(IndexApi, '/')
api.add_resource(HomeHeadApi, '/home/heads/')
api.add_resource(HomeDataApi, '/home/list/')

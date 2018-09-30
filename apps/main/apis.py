from flask_restful import Resource, fields, marshal_with, marshal

from apps.comm.result import Result
from apps.home.apis import result
from apps.main.models import User


# 对返回值处理
class IndexApi(Resource):
    @marshal_with(result)
    def get(self):
        users = User.query.all()
        return Result.to_success(users)

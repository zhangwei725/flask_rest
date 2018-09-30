from flask import request
from flask_restful import Resource, reqparse

# python
from apps.main.models import User

""""
参数 restful
# 添加参数
# 在请求中获取参数

参数类型
1>普通参数  
2>必要参数
3>一键多值[列表]
4>位置参数








"""


class Demo(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        """
        arg:传递参数的key
        type: int str
        help: 错误的提示信息
        default 参数默认值
        required 必要
        action 'append'
        location 位置参数 args form   files   headers  
        """

        self.parser.add_argument('uid', type=str, default=1)
        #     添加必要参数
        # self.parser.add_argument('page', type=int, required=True, help='必要参数')
        # 列表
        # 所有选中购物车的id ids = [1,2,3,4,5,6]
        # self.parser.add_argument('page', type=int, required=True, help='必要参数')
        # self.parser.add_argument('ids', type=int, required=True, action='append', location='heads')
        self.parser.add_argument('auth', type=str, location='headers')

    def get(self):
        # 字典对象
        # request.form
        args = self.parser.parse_args()
        # s = request.headers['auth']
        # request.values.get()
        # args.get()
        return u'测试参数'


# 路由 api.add_resource(Demo1, '/args/d1/<uid>')
# 请求路径  /args/d1/11/
class Demo1(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('create_date', type=int, default=0)

    def get(self):
        # 1 表示降序  0表示默认排序
        order = self.parser.parse_args().get('create_date')
        price_order = self.parser.parse_args().get('price')
        query = User.query
        if price_order:
            query.order_by(User.price)
        if order:
            query.order_by(User.create_date)
        users = query.all()
        return users

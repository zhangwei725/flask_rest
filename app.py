from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)

# 1> 安装 pip install flask-restful
# 2> 实例化
api = Api(app=app)
# 3  注册
"""
js框架
"""


# 对象不能转化成

# 定义视图层
class IndexResource(Resource):
    def get(self):
        # 获取参数
        # 数据库操作
        # 返回json数据
        return 'restful ---> get '

    def post(self):
        return 'restful ---> post '

    def put(self):
        return 'restful ---> put '


# 注册资源
#  别名  url_for('index')
api.add_resource(IndexResource, '/index/', '/', endpoint='index')

if __name__ == '__main__':
    app.run()

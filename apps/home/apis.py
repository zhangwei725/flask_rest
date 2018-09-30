from flask_restful import Resource, fields, marshal_with

from apps.comm.result import Result
from apps.home.models import Navigation, Category, Banner

"""
返回json数据
1> @marshal_with
2> marshal
返回数据的格式
1>可以列表 []
2>可能是对象{}(通常是这种)
第一种
{
 'code': 200
 'msg':'success'
 'data':[{
        'addresses':[]
 },{}]
}
第二种
{
 'code': 200
 'msg':'success'
 'data':{
    返回的数据是多个对象,但不是同一个对象
    nav:[],
    cate:[],
    banners:[]
 }
}
"""
nav_fields = {
    'nav_id': fields.Integer,
    'nav_name': fields.String,
}
cate_fields = {
    'cate_id': fields.Integer,
    'name': fields.String,
}
banners_fields = {
    'banner_id': fields.Integer,
    'title': fields.String,
    'image': fields.String,
    'detail_url': fields.String,
    'order': fields.Integer,
    'create_time': fields.DateTime(dt_format='iso8601'),
}
data_fields = {
    'navs': fields.List(fields.Nested(nav_fields)),
    'cates': fields.List(fields.Nested(cate_fields)),
    'banners': fields.List(fields.Nested(banners_fields))
}
result = {
    'code': fields.Integer(default=200),
    'msg': fields.String(default='success'),
    'data': fields.Nested(data_fields)
}

class HomeHeadApi(Resource):
    @marshal_with(result)
    def get(self):
        navs = Navigation.query.all()
        cates = Category.query.all()
        banners = Banner.query.all()
        return Result.to_success({
            'navs': navs,
            'cates': cates,
            'banners': banners
        })


class HomeDataApi(Resource):

    def get(self):
        return ''



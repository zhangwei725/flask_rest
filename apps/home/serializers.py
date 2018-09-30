from flask_restful import fields

user_fields = {
    'user_id': fields.Integer,
    'username': fields.String,
    'create_date': fields.DateTime,
    # 'addresses': fields.List(fields.Nested(address_fields)),
}

result = {
    'status': fields.Integer(),
    'msg': fields.String,
    "data": fields.List(fields.Nested(user_fields)),
    # "data": fields.Nested(user_fields)
}

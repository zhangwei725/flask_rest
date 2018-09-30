# 字段
# 普通字段
# 静态字段

# 方法
# 对象方法
# 类方法
# 静态方法

# 属性
# 使用的是的字段
# 声明的时候是方法
#
RESULT_SUCCESS_CODE = 200
RESULT_SUCCESS_MSG = 'success'


class Result:
    @staticmethod
    def to_success(data, status=RESULT_SUCCESS_CODE, msg=RESULT_SUCCESS_MSG):
        result = {
            'status': status,
            'msg': msg,
            'data': data
        }
        return result

    @staticmethod
    def to_error(status=404, msg='error'):
        result = {
            'status': status,
            'msg': msg,
        }
        return result

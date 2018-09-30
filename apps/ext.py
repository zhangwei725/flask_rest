# 第三方扩展插件的配置文件
# =====数据库配置=======
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 数据库操作核心对象
db = SQLAlchemy()
# 数据库迁移对象
migrate = Migrate()


#
def init_ext(app):
    init_db(app)


def init_db(app):
    # 配置数据库连接
    config_db(app)
    db.init_app(app=app)
    migrate.init_app(app, db)


# 配置数据库的参数
def config_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/tmall'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 设置请求结束之后自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

from flask import Flask

app = Flask(__name__)
app.debug = True
from .home import home as home_blueprint

app.register_blueprint(home_blueprint, url_prefix='/home')  # url_prefix是访问蓝图的链接前缀如：www.abc.com/admin

from .admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')  # url_prefix是访问蓝图的链接前缀如：www.abc.com/admin

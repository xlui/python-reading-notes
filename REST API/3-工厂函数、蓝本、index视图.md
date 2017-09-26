## 首先创建工厂函数。

> 工厂函数用来创建程序实例，注册蓝本。

示例1 `app/__init__.py`：程序包的构造文件
```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    return app
```

## 接着创建蓝本

示例2 `app/api_1_0/__init__.py`：创建蓝本
```python
from flask import Blueprint

api = Blueprint('api', __name__)

from . import views
```

程序的路由保存在 `app/api_1_0/views.py` 模块中，导入该模块就能把路由和蓝本关联起来。注意，模块要在 `app/api_1_0/__init__.py` 脚本的末尾导入，这是为了避免循环导入依赖，因为在 `views` 中还要导入 `api_1_0`。

## 注册蓝本

示例3 `app/__init__.py`：注册蓝本

```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .api_1_0 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')
    # url_prefix 参数是对蓝本的所有路由添加前缀
    
    return app
```

## index 视图

示例4 `app/api_1_0/views.py`：视图

```python
from . import api
from flask import jsonify

default_data = [
    {
        'id': 1,
        'title': 'Buy something',
        'description': 'Milk, Cheese, Pizza',
        'done': False
    },
    {
        'id': 2,
        'title': 'learn Python',
        'description': 'need to find a good Python tutor',
        'done': False
    }
]

@api.route('/', methods=['GET'])
def index():
    return jsonify({'tasks': default_data})
```

## 启动脚本

示例5 `manage.py`：启动脚本
```python
from app import create_app
from flask_script import Manager, Shell

app = create_app()
manager = Manager(app)


if __name__ == '__main__':
    @manager.command
    def shell():
        return dict(app=app)

    manager.run()
```

## 运行程序

运行：  
`python manage.py runserver`  
GET 数据：  
`curl 127.0.0.1:5000/api/v1.0` 或者访问 `http://127.0.0.1:5000/api/v1.0`

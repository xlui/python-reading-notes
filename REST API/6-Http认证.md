HTTP 认证协议很简单，可以直接实现，不过 Flask-HTTPAuth 扩展提供了一个便利的包装，可以把协议的细节隐藏在修饰器之中，类似于 Flask-Login 提供的 login_required 修
饰器。

在将 HTTP 基本认证的扩展进行初始化之前，我们先要创建一个 HTTPBasicAuth 类对象。和 Flask-Login 一样，Flask-HTTPAuth 不对验证用户密令所需的步骤做任何假设，因此所需的信息在回调函数中提供。

示例10 `app/api_1_0/views.py`

```python
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username == 'ok' and password == 'python':
        return True
    return False

@auth.error_handler
def auth_error():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

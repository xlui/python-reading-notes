## 获取特定 id 的 task

只需要添加支持获取 id 的路由即可。

示例6 `app/api_1_0/views.py`
```python
from flask import abort, make_response

@api.route('/<ind:id>', methods=['GET'])
def get_task(id):
    task = [t for t in default_task if t.get('id') == id]
    if not task:
        abort(404)
    return jsonify({'task':task})

@api.app_errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': "Not Found"}), 404)
```

如果没有在 `default_task` 中找到 id 对应的 task ，则中断并返回 404 错误。用 `api.app_errorhandle` 修饰符处理错误。

## 测试

运行：  
`python manage.py runserver`  
访问：  
`127.0.0.1:5000/api/v1.0/1`  
`127.0.0.1:5000/api/v1.0/2`  
`127.0.0.1:5000/api/v1.0/3`  

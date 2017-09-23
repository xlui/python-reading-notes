如果页面上只有简单的表单，并且视图函数定义了 Get、Post方法。当用户输入后提交表单，然后点击浏览器的刷新按钮，会看到一个莫名其妙的警告，要求在再次提交表单之前进行确认。之所以出现这种情况，是因为刷新页面时浏览器会重新发送之前已经发送过的最后一个请求。如果这个请求是一个包含表单数据的 POST 请求，刷新页面后会再次提交表单。大多数情况下，这并不是理想的处理方式。

很多用户都不理解浏览器发出的这个警告。基于这个原因，最好别让 Web 程序把 POST 请求作为浏览器发送的最后一个请求。

这种需求的实现方式是，使用重定向作为 POST 请求的响应，而不是使用常规响应。重定向是一种特殊的响应，响应内容是 URL，而不是包含 HTML 代码的字符串。浏览器收到这种响应时，会向重定向的 URL 发起 GET 请求，显示页面的内容。这个页面的加载可能要多花几微秒，因为要先把第二个请求发给服务器。除此之外，用户不会察觉到有什么不同。现在，最后一个请求是 GET 请求，所以刷新命令能像预期的那样正常使用了。这个技巧称为 `Post/重定向/Get 模式`。

但这种方法会带来另一个问题。程序处理 POST 请求时，使用 form.name.data 获取用户输入的名字，可是一旦这个请求结束，数据也就丢失了。因为这个 POST 请求使用重定向处理，所以程序需要保存输入的名字，这样重定向后的请求才能获得并使用这个名字，从而构建真正的响应。

程序可以把数据存储在用户会话中，在请求之间“记住”数据。用户会话是一种私有存储，存在于每个连接到服务器的客户端中。

示例：
```python
from flask import Flask, render_template, session, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

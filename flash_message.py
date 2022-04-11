# 闪现系统使得在一个请求结束的时候记录一个信息，并且在下次（且仅在下一次中）请求时访问它，这通常与布局模板结合使用以公开信息。
from unicodedata import category

from flask import get_flashed_messages


flask(message,category)

#message 参数是要闪现的实际消息。
#category 参数是可选的。它可以是“error”，“info”或“warning”。

#从会话中删除消息
get_flashed_messages(with_categories,category_filter)

模板
{% with message = get_flashed_messages()%}
    {% if message %}
        {%for message in messages %}
            {{message}}
        {% endfor %}
    {% endif %}
{% endwith %}    
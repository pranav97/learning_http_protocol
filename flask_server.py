from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask import request
import time
import functools

app = Flask(__name__)
auth = HTTPBasicAuth()

logs = None

class LogsSystem:
    all_logs = []

    def addHeader(self, single_head):
        self.all_logs.append(single_head)

    def get_html(self):
        html_list = """"""
        for i in self.all_logs:
            html_list += """<li><p class="date"> {} </p><p> {} </p></li>""".format(i.local_time, i.headers_string)
        return html_list


class SingleHeader:
    headers_string = ""
    local_time = ""
    def __init__(self, header_str):
        self.local_time = time.asctime(time.localtime())
        self.headers_string = header_str



users = {
    "pranav": "slug",
    "user": "easy"
}

def log_headers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret_val = func(*args, **kwargs)
        header_str = ""
        for key, value in request.headers.to_wsgi_list():
            header_str += "<p>{}: {}</p>".format(key, value)
        logs.addHeader(SingleHeader(header_str))
        return ret_val
    return wrapper


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/logs')
@auth.login_required
@log_headers
def print_all_logs():
    return """
    <h1> This is all the requests that came up until this one right here </h1>
    <ul id="stuff">
        {}
    <ul>
    """.format(logs.get_html())




@app.route('/')
@auth.login_required
@log_headers
def index():
    return "<h1>Hello, %s!</h1>" % auth.username()


if __name__ == '__main__':
    logs = LogsSystem()
    app.run(host='0.0.0.0', port=8080)

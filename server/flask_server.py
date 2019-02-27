from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
from flask_httpauth import HTTPBasicAuth
import time, functools, json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, City

app = Flask(__name__)


engine = create_engine('sqlite:///city.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

auth = HTTPBasicAuth()

logs = None


users = {
    "pranav": "slug",
    "user": "easy"
}


class SingleHeader:
    headers_string = ""
    local_time = ""
    def __init__(self, header_str):
        self.local_time = time.asctime(time.localtime())
        self.headers_string = header_str


class LogsSystem:
    all_logs = [] # the whole point of this all logs is to store a bunch of headers

    def addHeader(self, single_head):
        self.all_logs.append(single_head)

    def get_html(self):
        html_list = ""
        for i in self.all_logs:
            html_list += """<li><p class="date"> {} </p><div class="request"> {} </p></li>""".format(i.local_time, i.headers_string)
        return html_list

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

# How to make a restful api in flask

# These request verbs are:

# GET: fetch an existing resource. The URL contains all the necessary information the server needs to locate and return the resource.
# POST: create a new resource. POST requests usually carry a payload that specifies the data for the new resource.
# PUT: update an existing resource. The payload may contain the updated data for the resource.
# DELETE: delete an existing resource.

def addCity(cityName):
    session = DBSession()
    newCity = City(name=cityName)
    session.add(newCity)
    session.commit()


@app.route('/add_city', methods=["POST", "GET"])
# @auth.login_required
@LogsSystem.log_headers
def postCityName():
    session = DBSession()
    if request.method == 'POST':
        addCity(request.form['name'])
        data = {"Worked": "True"}
        return jsonify(data), 201
    else:
        return render_template('newCity.html')


@app.route('/cities')
# @auth.login_required
@LogsSystem.log_headers
def getCityNames():
    session = DBSession()
    cities = session.query(City).all()
    d = {"Cities": [city.name for city in cities]}
    return json.dumps(d), 200, {'Content-Type': 'application/json'}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/logs')
@auth.login_required
@LogsSystem.log_headers
def print_all_logs():
    return """
    <h1> This is all the requests that came up until this one right here </h1>
    <ul id="stuff">
        {}
    <ul>
    """.format(logs.get_html())


@app.route('/')
@auth.login_required
@LogsSystem.log_headers
def index():
    return "<h1>Hello, %s!</h1>" % auth.username()

if __name__ == '__main__':
    logs = LogsSystem()
    app.run(host='0.0.0.0', port=8080)

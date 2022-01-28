"""control dependencies to support CRUD routes and APIs"""
from flask import Blueprint, render_template
from flask_restful import Api, Resource
import requests

from page.pagesql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects

app_page_api = Blueprint('page_api', __name__,
                         url_prefix='/page_api',
                         template_folder='templates/page/',
                         static_folder='static',
                         static_url_path='static')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_page_api)


# Method #2 for page
@app_page_api.route('/')
def page_api():
    """obtains all Users from table and loads Admin Form"""
    return render_template("page_async.html", table=pages_all())


""" API routes section """


class PagesAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, display):
            po = Pages(name, display)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or {display} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return pages_all()

    # class for delete
    class _ReadID(Resource):
        def get(self, pageid):
            po = page_by_id(pageid)
            if po is None:
                return {'message': f"{pageid} is not found"}, 210
            data = po.read()
            return data

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return pages_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, display, name):
            po = page_by_display(display)
            if po is None:
                return {'message': f"{display} is not found"}, 210
            po.update(name)
            return po.read()

        # class for update/put

    class _UpdateName(Resource):
        def put(self, pageid, name):
            po = page_by_id(pageid)
            if po is not None:
                po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, display, name):
            po = page_by_display(display)
            if po is None:
                return {'message': f"{display} is not found"}, 210
            po.update(name)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, pageid):
            po = page_by_id(pageid)
            if po is None:
                return {'message': f"{pageid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:display>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadID, '/read/<int:pageid>')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:display>/<string:name>')
    api.add_resource(_UpdateName, '/update/<int:pageid>/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:display>/<string:name>')
    api.add_resource(_Delete, '/delete/<int:pageid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/page_api'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/1', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/read/4', "get"],
        ['/delete/5', "delete"],
        ['/read/5', "get"],
        ['/update/1/Thomas Alva Edison', "put"]
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Pages table")
    for page in pages_all():
        print(page)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()

from flask import Flask, request, Response
import pymongo
from bson import json_util
from machineMax.settings import MONGO_URI, MONGO_DB
import json

app = Flask(__name__)

mongo_uri = MONGO_URI
mongo_db = MONGO_DB
conn = pymongo.MongoClient(
    mongo_uri,
    27017
)
db = conn[mongo_db]


@app.route('/')
def articles():
    """
        GET API to return all the articles stored in mongodb.

        Returns
        -------
        JSON
            flask.Response of JSON containing all articles stored in the mongodb

    """

    result = db.articles.find()
    return Response(
        json_util.dumps({
            'status': 'success',
            'count': result.count(),
            'results': result}),
        mimetype='application/json'
    )


@app.route('/search')
def search_content():
    """
        GET API to return filtered articles based on query params

        Examples
        --------

        Sample URL to filter articles http://<hostname>/search?query=<>

        Returns
        -------
        JSON
            flask.Response of JSON containing all articles stored in the mongodb

    """
    query = request.args.get("query", "")
    # print(query, flush=True)
    query = query.replace(" ", "|")

    result = db.articles.find({"content": {"$regex": query, "$options": "ig"}})

    return Response(
        json_util.dumps({
            'status': 'success',
            'count': result.count(),
            'results': result}),
        mimetype='application/json'
    )


@app.errorhandler(404)
def page_not_found(e):
    """
            404 Error handler.

            Returns
            -------
            JSON
                400 status with bad request response

        """
    return 'bad request!', 400


if __name__ == '__main__':
    app.run()

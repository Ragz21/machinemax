from flask import Flask, request, Response
import pymongo
from bson import json_util
import json

app = Flask(__name__)

# CReate mongo connection
mongo_uri = 'mongodb+srv://machineMax:<password>@cluster0.wmlolkb.mongodb.net/?retryWrites=true&w=majority'
mongo_db = 'guardian'
conn = pymongo.MongoClient(
    mongo_uri,
    27017
)
db = conn[mongo_db]


@app.route('/')
def articles():
    """Gets all the articles"""
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
    """Gets the articles based on query, eg: http://<hostname>/search?query=qatar"""
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


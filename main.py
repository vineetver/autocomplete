from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
import os

app = Flask(__name__)

# Get Elasticsearch host and port from environment variables
es_host = os.getenv('ES_HOST', 'elasticsearch-service')
es_port = os.getenv('ES_PORT', '9200')
es = Elasticsearch([f"http://{es_host}:{es_port}"])

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    # Index data into "myindex"
    res = es.index(index='myindex', body=data)
    return jsonify(res)

@app.route('/search', methods=['GET'])
def search_data():
    # Get the query parameter (e.g., /search?q=keyword)
    query = request.args.get('q')
    # Perform a match query on the "content" field
    res = es.search(index='myindex', body={"query": {"match": {"content": query}}})
    return jsonify(res)

if __name__ == '__main__':
    # Expose on all interfaces and port 5000
    app.run(host='0.0.0.0', port=5000)


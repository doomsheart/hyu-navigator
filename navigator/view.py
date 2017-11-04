from flask import request
from navigator import app

import json
import maps


@app.route("/")
def hello_hack():
    return "Hello"


@app.route("/search")
def search_path():
    start_id = request.args.get('start_id', '')
    end_id = request.args.get('end_id', '')

    result = maps.path_search(int(start_id), int(end_id))
    return json.dumps(result)

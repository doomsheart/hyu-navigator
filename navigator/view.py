from flask import request
from navigator import app

import json
import maps


@app.route("/")
def hello_hack():
    return "Hello"


@app.route("/search")
def search_path():
    start_id = request.args.get('start_id', None)
    end_id = request.args.get('end_id', None)
    middle_id = request.args.get('middle_id', None)

    if start_id is None or end_id is None:
        return json.dumps({"response": "failure"})

    result = maps.path_search(int(start_id), int(end_id), [int(middle_id)])
    return json.dumps(result)

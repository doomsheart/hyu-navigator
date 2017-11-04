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

    middle_list = list()
    if middle_id is not None:
        middle_list.append(int(middle_id))

    result = maps.path_search(int(start_id), int(end_id), middle_list)
    return json.dumps(result)

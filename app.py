#!venv/bin/python

from flask import Flask, jsonify, abort, make_response, request, url_for
import sort

app = Flask(__name__)

data = {
    "PO123": {"lines": ["1.0", "1.1"]},
    "PO456": {"lines": ["4.0", "2.0"]},
    "PO789": {"lines": ["2.0", "3.0", "3.2", "3.1"]},
}

@app.route('/', methods=['GET'])
def get_pos():
    pos = [po for po in data.keys()]
    return jsonify(pos)

@app.route('/<string:po>', methods=['GET'])
def get_po(po):
    if po not in data:
        abort(404)
    to_sort = data[po]['lines']
    sorted = sort.quick_sort(to_sort, 0, len(to_sort) - 1)
    return jsonify(sorted)

@app.route('/<string:po>/<int:line>', methods=['GET'])
def get_po_line(po, line):
    if po not in data:
        abort(404)
    lines = data[po]['lines']
    if 0 >= line or line > len(lines):
        abort(404)
    return jsonify(lines[line - 1])

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify('Not found'), 404)

if __name__ == '__main__':
    app.run(debug=True)

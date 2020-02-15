from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from api import api

app = Flask(__name__)

cors = CORS(app)

api = api()

if __name__ == '__main__':
    app.run()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/drugs')
def drugs():
    return jsonify(list(api.product_list.keys()))


@app.route('/graph/')
@app.route('/graph/<path:molecule>')
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def graph(molecule: str = None):
    sample = {
        "nodes": [
            {"key": 0, "text": molecule, "color": "lightred"},
            *[{"key": key + 1, "text": text, "color": "lightblue"} for key, text in
              enumerate(api.product_list[molecule])]
        ],
        "links": [{"key": -key - 1, "from": 0, "to": key + 1} for key, _ in enumerate(api.product_list[molecule])],
    }
#     else:
#         sample = {
#             "nodes": [
#                 {"key": 0, "text": "Lepirudin", "color": "lightblue"},  # , "loc": "0 0"},
#                 {"key": 1, "text": "Beta"},  # , "color": "orange", "loc": "150 0"},
#                 {"key": 2, "text": "Gamma", "color": "lightgreen"},  # , "loc": "0 150"},
#                 {"key": 3, "text": "Delta", "color": "pink"},  # , "loc": "150 150"}
#             ],
#             "links": [
#                 {"key": -1, "from": 0, "to": 1},
#                 {"key": -2, "from": 0, "to": 2},
#                 {"key": -3, "from": 1, "to": 1},
#                 {"key": -4, "from": 2, "to": 3},
#                 {"key": -5, "from": 3, "to": 0}
#             ]
#         }

    return jsonify(sample)


if __name__ == '__main__':
    app.run()

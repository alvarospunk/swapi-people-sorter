from flask import Flask, jsonify
from .model import StarWarsModel
from .view import StarWarsView


app = Flask(__name__)


@app.route('/starwars/people', methods=['GET'])
def get_people():
    data = StarWarsModel.fetch_people_data()
    response, status = StarWarsView.format_response(data)
    return jsonify(response), status


if __name__ == '__main__':
    app.run(debug=True)

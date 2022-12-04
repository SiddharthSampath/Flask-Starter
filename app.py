import pickle

from flask import Flask, request, jsonify
from helpers import get_dict_tuples

app = Flask(__name__)


@app.route('/')
def hello_dear_flask():

    return 'Hello Dear Flask'


@app.route('/parameters', methods=['GET', 'POST'])
def process_parameters():
    """
    nutrient_n, nutrient_p, nutrient_k, temperature, humidity, pH, rainfall
    :return:
    """

    if request.method == 'POST':

        req_json = request.get_json()

        nutrient_n, nutrient_p, nutrient_k, temperature, humidity, ph, rainfall = get_dict_tuples(
            req_json, ['nutrient_n', 'nutrient_p', 'nutrient_k', 'temperature', 'humidity', 'ph', 'rainfall']
            )

        # if all you want to do is use write this to a file then you can remove the lines on top

        with open('dummy.pickle', 'wb') as f:
            pickle.dump(req_json, f, protocol=pickle.HIGHEST_PROTOCOL)

        return jsonify({'woo': 'hoo', 'all': 'done'})

    return 'GET request response'


if __name__ == '__main__':
    app.run(debug=True)

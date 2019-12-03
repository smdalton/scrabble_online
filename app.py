from flask import Flask
from flask import jsonify
from flask import request, make_response

import scrabble

app = Flask(__name__)


board = scrabble.ScrabbleBoard()



@app.route('/', methods=['GET'])
def hello_world():
    html = "<head>HomePage</head>"
    return make_response(jsonify(html),200)


@app.route('/is-valid-word', methods=['GET'])
def is_valid_word():
    word = request.args.get('word_attempt')
    return jsonify({'the word sent was': word})



@app.route('/debug', methods=['GET'])
def debug():
    return jsonify(
        {
        'board' : board.letter_dict,
        'current_bag':  board.get_bag()
        })


@app.route('/reset-bag', methods=['GET'])
def reset_bag():
    board.reset_bag()
    return 200


@app.route('/test', methods=['GET'])
def test():
    return "derp"


@app.route('/get-hand', methods=['GET'])
def get_hand():
    num_tiles = request.args.get('num_tiles')
    if num_tiles:
        return jsonify({'hand':board.get_hand(num_tiles)})
    else:
        return jsonify({'hand': 'error'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

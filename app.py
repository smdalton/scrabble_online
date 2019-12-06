from flask import Flask
from flask import jsonify
from flask import request, make_response
from flask_restful import Api

from classes import scrabble_board as scrabble

app = Flask(__name__)
api = Api(app)

board = scrabble.ScrabbleBoard()

@app.route('/', methods=['GET'])
def hello_world():
    html = "<head>HomePage</head>"
    return make_response(html,200)

@app.route('/is-valid-word', methods=['GET'])
def is_valid_word():
    word = request.args.get('check-word')
    return jsonify({'check-word': word,
                    'valid': 'true'})


@app.route('/debug', methods=['GET'])
def debug():
    return jsonify(
        {
        'board-dict' : board.letter_dict,
        'current-bag':  board.get_bag()
        })

@app.route('/reset-bag', methods=['GET'])
def reset_bag():

    if request.args.get('test'):
        old_board = board.get_bag()
        board.reset_bag()
        new_board = board.get_bag()
        response = make_response(
        jsonify(
            {
                'old-board': old_board,
                'new-board': new_board
            }),
        200
        )
        return response
    else:
        board.reset_bag()
        new_board = board.get_bag()
        response = make_response(
        jsonify(
            {
                'new-board': new_board
            }),
        200
        )
        return response

    return make_response('error in reset_bag')


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

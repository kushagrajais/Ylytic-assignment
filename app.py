from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://app.ylytic.com/ylytic/test"

@app.route('/search', methods=['GET'])
def search_comments():
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    # Build the parameters for the request to the original API
    params = {
        'search_author': search_author,
        'at_from': at_from,
        'at_to': at_to,
        'like_from': like_from,
        'like_to': like_to,
        'reply_from': reply_from,
        'reply_to': reply_to,
        'search_text': search_text
    }

    # Make a request to the original API
    response = requests.get(BASE_URL, params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import os

from get_comments import process_subreddit

app = Flask(__name__)
API_KEY = os.environ.get('API_KEY')

@app.route('/get_comments')
def index():
    api_key = request.headers.get('Apikey')

    if api_key is None:
        return jsonify({"message": "no apikey found in request"}), 401

    if api_key == API_KEY:
        subreddit = request.args.get('subreddit')
        comment_count = request.args.get('count', default=10)
        subreddit_comments = process_subreddit(subreddit, comment_count)
        return jsonify({
                   "comments": subreddit_comments,
                   "subreddit": subreddit
               }), 200
    else:
        return jsonify({"message": "ERROR...WRONG KEY"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0')

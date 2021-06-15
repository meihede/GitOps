from flask import Flask, render_template, json, jsonify
import json, os

app = Flask(__name__, template_folder='.')

data = {'message': 'hello world html'}


@app.route('/')
def index():
    return render_template('index.html', title='home page', jsonfile=json.dumps(data))


@app.route('/api', methods=['GET'])
def defaultApi():
    return jsonify(data), 200


@app.route('/api/<name>', methods=['GET'])
def api(name):
    if name is not None:
        data['message'] = 'hello ' + name
    return jsonify(data), 200


if __name__ == '__main__':
    port = os.environ.get('PORT', 80)
    app.run(debug=False, host='0.0.0.0', port=port)

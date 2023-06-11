from flask import Flask, jsonify, render_template, request
from redis.cluster import RedisCluster

app = Flask(__name__)
rd = RedisCluster(host="redis-cluster", port=6379, decode_responses=True)
app.config['JSONIFY_PRETTYPRINT_RE1GULAR'] = False
click = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pregunta', methods=['POST'])
def _get_data():
    global click
    if (click < 5):
        key = 'preg' + str(click)
        click += 1
        return rd.get(key)
    return rd.get('preg5')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, jsonify, render_template, request
from redis.cluster import RedisCluster

app = Flask(__name__)
rd = RedisCluster(host="redis-cluster", port=6379, decode_responses=True)
app.config['JSONIFY_PRETTYPRINT_RE1GULAR'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pregunta', methods=['POST'])
def _get_data():
    key = request.form.get('nro')
    return rd.get(key)

@app.route('/save-score', methods=['POST'])
def save_score():
    sc = request.form.get('score')
    # Agregar el dato a la lista en Redis
    rd.lpush('scores', sc)
    # Obtener todos los datos almacenados en Redis
    scores = rd.lrange('scores', 0, -1)
    sc = float(sc)
    # Realizar operaciones con los datos
    scores = [float(_) for _ in scores]
    for _ in scores:
        if sc < _:
            return 'No estás en primer lugar.\n"No se metan a pensar si no están acostumbrados"\n--Alejandro Dolina'
    return 'Lograste el mayor puntaje!\n"El problema de la humanidad es que los estúpidos están seguros de todo y los inteligentes están llenos de dudas"\n--Bertrand Russell'

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)

from redis.cluster import RedisCluster
from random import randint

preguntas = [["Cuántas copas de Fútbol ganó Argentina? \nA: 2\nB: 3", "01"],
             ["Cuántas copas de Fútbol ganó Argentina? \nA: 3\nB: 1", "10"],
             ["Cuántas copas de Fútbol ganó Brasil? \nA: 2\nB: 5","01"]]

rd = RedisCluster(host="redis-cluster", port=6379)

while (True):

    if rd.get('preg') == None:
        pregunta = preguntas[randint(0,2)]
        pregunta = "==".join(pregunta)
        rd.set('preg', pregunta)

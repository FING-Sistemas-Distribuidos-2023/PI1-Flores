from redis.cluster import RedisCluster

preguntas = [
    {
        'pregunta': "¿Cuántas copas de Fútbol ganó Uruguay?\nA: 4\nB: 2",
        'respuesta': "01"
    },
    {
        'pregunta': "Linus Torvalds tiene un grado de\nA: Computer Science papá\nB: Grado de nada, es un genio como Bill Gates que dejó Harvard",
        'respuesta': "10"
    },
    {
        'pregunta': "¿Qué es más importante en programación: la elegancia del código o la eficiencia?\nA: Ambas\nB: Ninguna, solo que funcione",
        'respuesta': "01"
    },
    {
        'pregunta': "En el debate entre la inteligencia artificial y la inteligencia humana, ¿quién ganará a largo plazo?\nA: La inteligencia artificial\nB: La estupidez natural",
        'respuesta': "11"
    }
]

def generar_pregunta():
    try:
        rd = RedisCluster(host="redis-cluster", port=6379)

        if rd.ping():
            print("Conexión exitosa con el clúster Redis.")
        if rd.get('scores') != None:
            rd.delete('scores')

        while(True):

            if rd.get('preg1') is None:
                pregunta = preguntas[0]
                pregunta_str = f"{pregunta['pregunta']}=={pregunta['respuesta']}"
                rd.set('preg1', pregunta_str)
            if rd.get('preg2') is None:
                pregunta = preguntas[1]
                pregunta_str = f"{pregunta['pregunta']}=={pregunta['respuesta']}"
                rd.set('preg2', pregunta_str)
            if rd.get('preg3') is None:
                pregunta = preguntas[2]
                pregunta_str = f"{pregunta['pregunta']}=={pregunta['respuesta']}"
                rd.set('preg3', pregunta_str)
            if rd.get('preg4') is None:
                pregunta = preguntas[3]
                pregunta_str = f"{pregunta['pregunta']}=={pregunta['respuesta']}"
                rd.set('preg4', pregunta_str)
            if rd.get('preg5') is None:
                rd.set('preg5', "No hay más preguntas, o querés seguir humillándote?")
    except Exception as e:
        print(f"Error al conectarse al clúster Redis: {str(e)}")

# Ejecutar la función para generar una pregunta y verificar la conexión
generar_pregunta()

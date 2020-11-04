import pg8000
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    connection = pg8000.connect(os.environ['DB_USER'], password=os.environ['DB_PASSWORD'], port=os.environ['DB_PORT'], host=os.environ['DB_HOST'])
    s = connection.run("SELECT 'Hello, my dear!'")
    return "Задание 4. Использование Docker с БД, Кластеризация! Info: {}".format(*s[0])

import time
from flask import Flask, jsonify
import random
app = Flask(__name__)
list0=['motor0','motor1','motor2','motor3','sensor0','sensor1','sensor2','sensor3']
list1=['motor4','motor5','motor6','sensor4','sensor5','sensor6','sensor7']
def random_s():
    dic = {}
    for i in range(8):
        dic[str(list0[i])] = str(random.randrange(2))
    return dic

def random_n():
    dic = {}
    for i in range(7):
        dic[str(list1[i])] = str(random.randrange(2))
    return dic

@app.route('/s/status/')
def status_s():
    d=random_s()
    return jsonify(d)

@app.route('/n/status/')
def status_n():
    d=random_n()
    return jsonify(d)

if __name__ == '__main__':
    app.run(port=5000)


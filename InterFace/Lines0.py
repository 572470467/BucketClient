import time
from flask import Flask, jsonify
import random
app = Flask(__name__)
list=[{'pos':0,'sensors':[0,1,1,1,1]},{'pos':1,'sensors':[1,0,1,1,1]},{'pos':2,'sensors':[1,1,0,1,1]},{'pos':3,'sensors':[1,1,1,0,1]},{'pos':4,'sensors':[1,1,1,1,0]}]
def random_status():
    dic = {}
    for i in range(2):
        dic[str(i)] = str(random.randrange(5))
    return dic[str(i)]

@app.route('/carrier/status')
def status():
    d=list[int(random_status())]
    return jsonify(d)

@app.route('/carrier/moveto/<groupid>')
def moveto(groupid):
    d=groupid
    return jsonify(d)

if __name__ == '__main__':
    app.run(port=5000)


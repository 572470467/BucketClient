import time
from flask import Flask, jsonify
import random
app = Flask(__name__)
text=['正在运行甲工序...','正在运行乙工序...','正在运行丙工序...','正在运行丁工序...','正在运行戊工序...']
list=[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]

def random_status():
    dic = {}
    for i in range(2):
        dic[str(i)] = str(random.randrange(5))
    return list[int(dic[str(i)])]

@app.route('/mixer/<groupid>')
def button(groupid):
    d=list[int(groupid[0])]
    num=int(groupid[0])
    d=text[num]
    return jsonify(d)

@app.route('/mixerstatus/')
def status():
    d={'status':random_status()}
    return jsonify(d)

if __name__ == '__main__':
    app.run(port=5050)


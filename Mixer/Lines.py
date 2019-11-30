import time
import Mix_group
from common import Carrier
from flask import Flask, jsonify
import random
app = Flask(__name__)
list=[{'pos':0,'sensors':[0,1,1,1,1]},{'pos':1,'sensors':[1,0,1,1,1]},{'pos':2,
'sensors':[1,1,0,1,1]},{'pos':3,'sensors':[1,1,1,0,1]},{'pos':4,'sensors':[1,1,1,1,0]}]
list0=[[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
CGQ=[[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,0]]
def random_A():
    dic = {}
    for i in range(2):
        dic[str(i)] = str(random.randrange(7))
    return list0[int(dic[str(i)])]

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
    d=int(groupid)
    car=Carrier([13,6,5,0,11], 18, 23, 12, 25, 20, 24)
    return str(car.moveto(d))

@app.route('/mixer/<groupid>')
def button(groupid):
    B=Mix_group
    if groupid=='000':
        return str(B.catch_powder())
    elif groupid=='100':
        return str(B.mixed_powder())
    elif groupid=='200':
        return str(B.powder_feeding())
    elif groupid=='300':
        return str(B.mixed_abrasive())
    elif groupid=='400':
        return str(B.make_wetting_agent())
    elif groupid=='500':
        return str(B.add_wetting_agent())
    elif groupid=='600':
        return str(B.abrasive_feeding())
                                                                               \

@app.route('/mixerstatus/')
def status_A():
    d={'status':random_A()}
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)



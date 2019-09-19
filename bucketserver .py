from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

releasestart = {'a':0, 'b':0}
releaseend = {'a':0, 'b':0}
releaseactive = {'a': False, 'b': False}

def random_status(cnt):
    dic = {}
    for i in range(cnt):
        dic[str(i)] = str(random.randrange(2)) + str(random.randrange(2))
    return dic

@app.route('/bucketgroup/a')
def group_a():
    d = random_status(5)
    return jsonify(d)

@app.route('/bucketgroup/b')
def group_b():
    d = random_status(4)
    return jsonify(d)

@app.route('/feederon/<groupid>')
def feeder_release(groupid):
    if groupid in releasestart.keys():
        releasestart[groupid] = releaseend[groupid] = time.time()
        releaseactive[groupid] = True
        d = {'status': 'OK'}
    else:
        d = {'status': 'Error'}
    return jsonify(d)

@app.route('/feederoff/<groupid>')
def feeder_stop(groupid):
    if groupid in releasestart.keys():
        releaseend[groupid] = time.time()
        releaseactive[groupid] = False
        d = {'status': 'OK'}
    else:
        d = {'status': 'Error'}
    return jsonify(d)

@app.route('/scale/<groupid>')
def scale_read(groupid):
    if groupid in releasestart.keys():
        if releaseactive[groupid]:
            amt = time.time() - releasestart[groupid]
        else:
            amt = releaseend[groupid] - releasestart[groupid]
        d = {'status': 'OK', 'reading': amt, 'started':releasestart[groupid]}
    else:
        d = {'status': 'Error', 'reading': -1, 'started': -1}
    return jsonify(d)

if __name__ == '__main__':
    app.run()


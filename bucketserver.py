from flask import Flask, jsonify
import random

app = Flask(__name__)

def random_status(cnt):
    dic = {}
    for i in range(cnt):
        dic[str(i)] = str(random.randrange(2)) + str(random.randrange(2))
    return dic

@app.route('/bucketgroup/a')
def group_a():
    d = random_status(5)
    print(d)
    return jsonify(d)

@app.route('/bucketgroup/b')
def group_b():
    d = random_status(4)
    print(d)
    return jsonify(d)

if __name__ == '__main__':
    app.run()


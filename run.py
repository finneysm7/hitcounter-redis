import flask
import json
import sys
import redis
import os
from multiprocessing import Value

hosts = open('/etc/hosts','r')
for line in hosts:
    if 'redis' in line:
        host = line.split()[0]

pool = redis.ConnectionPool(host=host,port=6379,db=0)
r = redis.Redis(connection_pool=pool)

app = flask.Flask(__name__)
@app.route('/', methods=['GET'])
def show():
    counter = r.get('counter')
    if counter == None:
        print counter
        r.set('counter', str(1))
    else:
        value = int(counter)
        value += 1
        r.set('counter', str(value))
    return "This page has been visited {counter} times".format(counter=r.get('counter'))

app.run(host='0.0.0.0', debug = '--debug' in sys.argv, threaded = True)

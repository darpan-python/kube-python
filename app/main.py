from flask import Flask
from flask import request
from flask import jsonify
import os
from executor import Executor

app = Flask(__name__)
path = os.environ['FILE_PATH'] if 'FILE_PATH' in os.environ else ''

# path = "/home/darpan/Desktop/projects/project-kube/app/test.txt"
ex = Executor(path)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    ip = request.remote_addr
    val = request.headers['Sec-Ch-Ua-Platform'] if 'Sec-Ch-Ua-Platform' in request.headers else ''
    ex.write_file(ip,val)
    return "Hello World!, {} {}".format(ip,val)


@app.route('/list', methods=['GET', 'POST'])
def get_list():
    welcome()
    _list = ex.read_file()
    return jsonify(_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

from flask import Flask, request,jsonify
import sys
import importlib


sys.path.append('/')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    data = request.data.decode('utf-8') #request.data.decode('utf-8')
    file_name, func_name = data.split('||')
    prototype=''
    if '$$' in func_name:
        func_name, prototype = func_name.split('$$')

    results_view = importlib.import_module(file_name)
    if len(prototype)>0:
        result = getattr(results_view, func_name)(prototype)
    else:
        result = getattr(results_view, func_name)()

    result_dict = {'equation': result[0], 'solution': str(result[1])}  # преобразуем результат в словарь

    return jsonify(result_dict)  # сериализуем словарь в JSON и возвращаем его
    #return jsonify(result)

if __name__ == '__main__':
    app.run(port=5004, host='0.0.0.0')
import sys
import importlib

from flask import Flask, request, jsonify, make_response


sys.path.append('/')
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    task_url = request.form.get('url')
    if not task_url:
        return make_response(
            jsonify({'error': 'The url parameter must not be empty in form'}),
            400,
        )
    splited_data = task_url.split('||')
    if len(splited_data) != 2:
        return make_response(
            jsonify({'error': 'The url for function must contain ||'}),
            400,
        )
    file_name, func_name = splited_data
    prototype = ''
    if '$$' in func_name:
        func_name, prototype = func_name.split('$$')
    try:
        results_view = importlib.import_module(file_name)
        if len(prototype) > 0:
            result = getattr(results_view, func_name)(prototype)
        else:
            result = getattr(results_view, func_name)()
        return jsonify(result)
    except ModuleNotFoundError:
        return make_response(
            jsonify({'error': 'Invalid path file'}),
            400,
        )
    except AttributeError:
        return make_response(
            jsonify(
                {'error': f'Function {func_name} is not found in code or you '
                          f'wrote it wrong in url parameter'}
            ),
            400,
        )


if __name__ == '__main__':
    app.run(port=5004, host='0.0.0.0')

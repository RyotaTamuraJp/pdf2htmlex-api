from flask import Blueprint, abort, make_response, jsonify, Flask
import subprocess
import os

app = Flask(__name__)
convert = Blueprint('convert', __name__)


@convert.route('/convert/<target_file_name>', methods=['GET'])
def create_account(target_file_name):
    try:
        save_name, _ = os.path.splitext(target_file_name)
        cmd = (
            f"pdf2htmlEX --zoom 1.0 /workspace/{target_file_name}"
            f" ../workspace/{save_name}.html"
        )

        app.logger.info(f"Start Conversion: {target_file_name}")

        proc = subprocess.run(cmd.split(" "), shell=False)

        app.logger.info(f"End Conversion: {target_file_name}")

        if proc.returncode != 0:
            raise Exception("HTMLの変換に失敗しました。")

    except Exception as e:
        app.logger.error(f"Error: {target_file_name}")
        abort(500, f'{e}')

    else:
        app.logger.info(f"Success: {target_file_name}")
        data = {"code": 200, "message": "HTMLの変換に成功しました。"}
        return make_response(jsonify(data))

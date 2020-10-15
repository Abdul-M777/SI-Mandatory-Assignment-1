from flask import Flask, Response
from flask import request, jsonify
from os import path
import sqlite3
import random
import datetime
from pathlib import Path
import json


# Init server
app = Flask(__name__)


def check_if_user_exits(conn, nemId, nemIdCode):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE NemID=? AND Password=?", (nemId, nemIdCode))
        # fetch the user if found
        db_result = cursor.fetchone()
        if db_result is None:
            raise ValueError('No user found')
        else:
            return db_result[0]
    except Exception as e:
        print(e)




@app.route('/nemid-auth', methods=['POST'])
def generate_nemId():
    nemIdCode = request.json['nemIdCode']
    nemId = request.json['nemId']

    conn = sqlite3.connect("../NemID_ESB/nem_id_database.sqlite")
    with conn:
        user_id = check_if_user_exits(conn, nemId, nemIdCode)
        if user_id is not None:
            generated_code = random.randint(100000, 999999)
            response_body = {
            "generatedCode": f"{generated_code}"
            }
        # Response
            response = Response()
            response.status_code = 200
            response.data = json.dumps(response_body)
            return response
            return jsonify({"authError": "forbidden access"}), 403


# Run app
if __name__ == "__main__":
    # Start server
    app.run(port = 8090)
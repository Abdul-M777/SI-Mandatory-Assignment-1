from flask import request, Response, Flask
import json
import random
import sqlite3


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/nemid-auth", methods=["POST"])
def authentication_nem_id():

    # exstract data
    nemIdCode = request.json.get("nemIdCode")
    nemId = request.json.get("nemId")

    if (nemId is None or nemIdCode is None):
        # create response body
        response_body = {
            "status": "Missing parameters",
            "error_message" : "To generate a nemID you need to specify a nemIdCode and email"
        }
    db = sqlite3.connect('../NemID_ESB/nem_id_database.sqlite')
    
    db_cursor = db.cursor()
    query = """SELECT Password FROM user WHERE NemID = """+nemId
    db_result = db_cursor.execute(query)
    db_pass = db_cursor.fetchone()
    if (db_pass == nemIdCode):
    # create response body
        response_body = {
            "generatedCode": random.randint(100000,999999)}
    # create response
        response = Response()
        response.status_code = 200
        response.data = json.dumps(response_body)
        return response
    else:
        response_body = {
            "status": "403",
            "error_message" : "Forbidden"
        }
        # create response
        response = Response()
        response.status_code = 403
        response.data = json.dumps(response_body)

if __name__ == "__main__":
    # begin server
    app.run(port = 8090)


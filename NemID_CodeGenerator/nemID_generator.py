from flask import request, Response, Flask
import json
import random
import sqlite3

# Create an instance of the flask class
app = Flask(__name__)

# URL
@app.route("/nemid-auth", methods=["POST"])
def authentication_nem_id():

    # Making a request and using a json decoder.
    nemIdCode = request.json.get("nemIdCode")
    nemId = request.json.get("nemId")

    # Check if the nemId or the nemIdCode is None.
        # Connect to the database.
    db = sqlite3.connect('../NemID_ESB/nem_id_database.sqlite')
    # Create a cursor
    db_cursor = db.cursor()
    # SQL statement
    query = """SELECT Id FROM user WHERE NemID = ? AND Password = ?"""
    db_result = db_cursor.execute(query,[nemId,nemIdCode])
    if (db_result == nemIdCode):
        response_body = {
            "generatedCode": random.randint(100000,999999)}
    # Response
        response = Response()
        response.status_code = 200
        response.data = json.dumps(response_body)
        return response
    else:
        response_body = {
            "status": "403",
            "error_message" : "Forbidden"
        }
        # Response
        response = Response()
        response.status_code = 403
        response.data = json.dumps(response_body)

if __name__ == "__main__":
    # Start Server
    app.run(port = 8090)


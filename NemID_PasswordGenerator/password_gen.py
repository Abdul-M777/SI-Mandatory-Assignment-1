from flask import request, Response, Flask, jsonify
import json
import random

# Create an instance of the flask class
app = Flask(__name__)

# URL
@app.route("/generate-password-nemID", methods=["POST"])
def password_generator():

    nemId = request.json["nemId"]
    cpr = request.json["cpr"]

    if (nemId is None or cpr is None):
        # Creating the response body
        response_body = {
            "status": "Missing parameters",
            "error_message" : "To generate a nemID you need to specify a cpr and email"
        }

        # Getting a response
        response = Response()
        response.status_code = 401
        response.data = json.dumps(response_body)
        return response
    else:
         
        first_2_digit_nemId = str(nemId)[:2]
        last_2_digit_cpr = str(cpr)[-2:]
        password = jsonify(str(first_2_digit_nemId)+str(last_2_digit_cpr))

        # Creating the response body
        response_body = {
            "nemIdPassword": f"{password}"
        }

        # Get a response.
        response = Response()
        response.status_code = 200
        response.data = json.dumps(response_body)
        return response

if __name__ == "__main__":
    # Start server
    app.run(port = 8089)


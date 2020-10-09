from flask import request, Response, Flask, jsonify
import json
import random


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/generate-password-nemID", methods=["POST"])
def api_password_generator():

    # exstract data
    nemId = request.json["nemId"]
    cpr = request.json["cpr"]

    if (nemId is None or cpr is None):
        # create response body
        response_body = {
            "status": "Missing parameters",
            "error_message" : "To generate a nemID you need to specify a cpr and email"
        }

        # create response
        response = Response()
        response.status_code = 401
        response.data = json.dumps(response_body)
        return response
    else:
        # generate random 5 digit code 
        first_2_digit_nemId = str(nemId)[:2]
        last_2_digit_cpr = str(cpr)[-2:]
        password = jsonify(str(first_2_digit_nemId)+str(last_2_digit_cpr))

        # create response body
        response_body = {
            "nemIdPassword": f"{password}"
        }

        # create response
        response = Response()
        response.status_code = 200
        response.data = json.dumps(response_body)
        return response

if __name__ == "__main__":
    # begin server
    app.run(port = 8089)


from flask import request, Response, Flask
import json
import random


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/generate-nemId", methods=["POST"])
def api_nemID_generator():

    # exstract data
    cpr = request.json["cpr"]

    if (cpr is None):
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
        random_digits = random.randint(10000, 99999)

        # create response body
        response_body = {
            "nemId": f"{random_digits}-{cpr[-4:]}"
        }

        # create response
        response = Response()
        response.status_code = 201
        response.data = json.dumps(response_body)
        return response

if __name__ == "__main__":
    # begin server
    app.run(port = 8088)
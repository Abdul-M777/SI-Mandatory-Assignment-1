from flask import request, Response, Flask
import json
import random

# Create an instance of the flask class
app = Flask(__name__)

# URL
@app.route("/generate-nemId", methods=["POST"])
# Generate a nemID
def api_nemID_generator():

    
    cpr = request.json["cpr"]

    if (cpr == None):
        # Creating the response body
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
        # Generate the random numbers
        random_digits = random.randint(10000, 99999)

        # creating the response body
        response_body = {
            "nemId": f"{random_digits}-{cpr[-4:]}"
        }

        # The response
        response = Response()
        response.status_code = 201
        response.data = json.dumps(response_body)
        return response

if __name__ == "__main__":
    # begin server
    app.run(port = 8088)
from flask import request, Response, Flask
import json
import random

# Create an instance of the flask class
app = Flask(__name__)

# URL
@app.route("/generate-nemId", methods=["POST"])
# Generate a nemID
def nemID_generator():

    # Making a request and using a json decoder.
    cpr = request.json["cpr"]

    # Generate the random numbers
    random_digits = random.randint(10000, 99999)

    # Creating the response body
    response_body = {
        "nemId": f"{random_digits}-{cpr[-4:]}"
        }

    # The response
    response = Response()
    response.status_code = 201
    response.data = json.dumps(response_body)
    return response

if __name__ == "__main__":
    # Start server
    app.run(port = 8088)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def scrape():
    # import your Python API and call the appropriate function/method
    from tests import json_string
    results = json_string

    # return the results
    return results



# To Run the aplication
# export FLASK_APP=app
# flask run
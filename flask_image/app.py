import json
from flask import Flask

app = Flask(__name__)

@app.route('/get/info')
def get_my_info():
    value = {
        "name": "Dany",
        "last_name": "Chavez",
        "social_media": [
            {"facebookUser": "Dany Chavez"},
            {"instagramUser": "Dfunn1k"},
            {"linkedinUser": 'dfunn1k'},

        ],
        "blog": "www.google.com",
        "author": "Dany Jesus"
    }

    return json.dumps(value)

if __name__ == '__main__':
    app.run(debug=True)
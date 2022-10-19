import requests
import json
import os
from dotenv import load_dotenv
from flask import Flask, render_template

app = Flask(__name__)

def configure():
    load_dotenv()

gif_list = []

def get_gifs():
    # set the apikey and limit
    apikey = os.getenv('api_key')  # click to set to your apikey
    lmt = 50    # set number of gifs to return MAX IS 50?
    ckey = "my_test_app"  # set the client_key for the integration and use the same value for all API calls

    search_term = "computers"
    
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        gif_json_data = json.loads(r.content)
        for each in gif_json_data['results']:
            gif = (each['media_formats']['gif']['url'])
            # gif_description = (each['content_description'])
            url = gif
            gif_list.append(url)
    else:
        gif_json_data = None


@app.route('/')
def index():
    current_gif = gif_list
    return render_template('index.html', current_gif=current_gif )

if __name__ == '__main__':
    get_gifs()
    app.run(debug=True, host='0.0.0.0')
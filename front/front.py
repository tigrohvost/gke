from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = 'http://back:5000/random'
    try:
        res = requests.get(url)
        result = res.text
    except:
        result = 'n/a'
    return result
    
if __name__ == "__main__":
    app.run()


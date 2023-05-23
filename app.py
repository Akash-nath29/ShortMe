from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=["GET", "POST"])
def shorten():
    url = request.form.get('text')
    try:
        try:
            result = tinyurl(url)
        except Exception:
            result = bitly(url)
    except Exception as e:
        return e
    return render_template("index.html", result = result)
    

def bitly(query):
    shortener = pyshorteners.Shortener(api_key='2ecb554e4668b29cb7332f3539294c8ba64339a2')
    shortenLink = shortener.bitly.short(query)
    return shortenLink

    

def tinyurl(query):
    shortener = pyshorteners.Shortener(api_key='0Oor30fhRt0NYaarnReNNOO6Fwqpa1MMerDW11nmh8PLMfBqlnBXSyJwTI7k')
    shortenLink = shortener.tinyurl.short(query)
    return shortenLink

    

if __name__ == '__main__':
    app.run(debug=True)

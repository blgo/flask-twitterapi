from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import dotenv
from twitterapi.gettwitts import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    # "setup" the session with starting values
    twitts = Twitts()
    try:
        twitts.authenticate()
        twitts.api.VerifyCredentials()
    except Exception:
        return render_template("error401.html")
    try:
        twitts.get_twitts()
    except Exception as error:
        return render_template("error.html", error=str(error))
    return render_template("index.html", twitts=twitts)


app.secret_key = '1Ai9Mk1fXnkN3VN1yTw445QZDokF4b'


if __name__ == "__main__":
     app.run(debug=True)

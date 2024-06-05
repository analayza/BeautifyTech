from flask import *

app = Flask(__name__)

@app.route("/politicasTermo")
def politicastermo():
    return render_template("politicasETermos.html")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
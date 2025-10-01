from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Salam, Flask khdama mzyan!"

if __name__ == "__main__":
    app.run(debug=True)
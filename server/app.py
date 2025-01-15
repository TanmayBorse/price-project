from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "HI"

if __name__ == "__main__":
    print("somthing")
    app.run()
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect("/static/index.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

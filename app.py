from flask import Flask, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/static/index.html")

@app.route('/create', methods = ['POST'])
def create():
    print request.method
    if request.method == 'POST':
        print request.form
    return "ok"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

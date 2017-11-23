from flask import Flask, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/static/index.html")

@app.route('/create', methods = ['POST'])
def create():
    #print "bookmark: " + request.form['bookmark']
    #print "tag: " + request.form['btag']
    #return str(request.form["bookmark"])
    return redirect("/static/new.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

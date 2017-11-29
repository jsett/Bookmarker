from flask import Flask, redirect, request
from rq import Queue
from redis import Redis
from jobs import count_words_at_url
app = Flask(__name__)

redis_conn = Redis()
q = Queue(connection=redis_conn)

@app.route('/')
def index():
    return redirect("/static/index.html")

@app.route('/create', methods = ['POST'])
def create():
    #print "bookmark: " + request.form['bookmark']
    #print "tag: " + request.form['btag']
    #return str(request.form["bookmark"])
    return redirect("/static/new.html")

@app.route('/reddittest', methods = ['GET'])
def reddittest():
    j = q.enqueue(count_words_at_url, 'http://reddit.com')
    return str(j.id)

@app.route('/redditres/<myid>', methods = ['GET'])
def redditres(myid):
    j = q.fetch_job(myid)
    return str(j.result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

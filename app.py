import datetime
import os
import psycopg2

from flask import Flask, render_template


def request_type (req):
    # Connect to database 
    conn = psycopg2.connect(host='db', database=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor() 
    d={}
    # Get number of all GET requests
    sql_request = """SELECT COUNT(*) FROM weblogs WHERE (source)='%s';"""  %req
    cur.execute(sql_request)
    total = cur.fetchone()[0]
    # Get number of all succesful requests
    sql_success = """SELECT COUNT(*) FROM weblogs WHERE status LIKE \'2__\'AND lower(source)='%s';""" %req
    cur.execute(sql_success)
    success = cur.fetchone()[0]
    # Store the result into dictionary for later lookup
    d["total"]=total 
    d["success"]=success
    return d

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def index(): 
    local = remote = "No entries yet!"
    d=request_type('local')
    if d["total"] != 0:
        local = str(d["success"] / d["total"])
    d=request_type('remote')
    if d["total"] != 0:
        remote = str(d["success"] / d["total"])
    return render_template('index.html', local = local, remote=remote)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

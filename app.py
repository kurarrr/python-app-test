'''This is test program'''
import MySQLdb
from flask import Flask,render_template,request

app=Flask(__name__)
db=MySQLdb.connect("localhost","root","","TEST1")
cursor=db.cursor()

log=[("名前","ログ")]

@app.route('/')
def index():
    '''indexページ'''
    return render_template('index.html',log=log)

@app.route('/write',methods=['GET'])
def write():
    poster=request.args.get("name","")
    text=request.args.get("text","")
    log.append((poster,text))
    return render_template('index.html',log=log)

@app.route('/dbwrite')
def dbwrite():
    com="select * from log"
    cursor.execute(com)
    for row in cursor:
        hoge.append((row[0],row[1],row[2]))
    return print(hoge[0][0],hoge[0][1],hoge[0][2])

app.run(debug=True)
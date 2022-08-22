from flask import Flask, render_template, request, abort
from threading import Thread
import sqlite3
import sys

app = Flask(__name__)

con = sqlite3.connect('tinker.db')
print("Opened database successfully")

con.execute("""CREATE TABLE IF NOT EXISTS users (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 user TEXT,
 user_id INTEGER UNIQUE);""")
print("Table created successfully")
con.close()

@app.route('/')
def home():
    return render_template('user.html')

@app.route('/webhook', methods = ['POST'])
def webhook():
   print("Recieved Webhook")
   sys.stdout.flush()
   if request.method == 'POST':
     print(request.json)
     return 'Success', 200
   else:
     abort(400)

@app.route('/newuser')
def new_user():
    return render_template('home.html')

@app.route('/stats')
def stats():
   return render_template('stats.html')

@app.route('/addrec', methods = ['POST','GET'])
def addrec():
     if request.method == 'POST':
       try:
         dn = request.form['dn']
         di = request.form['di']

         with sqlite3.connect("tinker.db") as con:
             cur = con.cursor()
             cur.execute("INSERT INTO users (user, user_id) VALUES (?,?)",(dn, di) )
            
             con.commit()
             msg = "Record successfully added"
             print(msg)
       except:
          con.rollback()
          msg = "error in insert operation"
      
       finally:
         if di == '425477636333240331':
           con.close()
           return render_template("result.html", msg = msg)
          
         if ((not dn) or (not di)):
           msg = "Please fill the required fields"

           return render_template("user.html", msg = msg)

         else:
           con.close()
           return render_template("thx.html", msg = msg)
     else:
       return render_template("user.html")

@app.route('/list')
def list():
    con = sqlite3.connect("tinker.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("select * from users")
   
    rows = cur.fetchall(); 
    return render_template("list.html",rows = rows)

@app.route('/doc')
def help_list():
    return render_template('documentation/docs.html')

@app.route('/rps')
def rps():
    return render_template('documentation/rps.html')

@app.route('/support')
def support():
    return render_template('documentation/support.html')

@app.route('/donate')
def donate():
    return render_template('documentation/donate.html')

@app.route('/don')
def don():
    return render_template('documentation/don.html')

@app.route('/work')
def work():
    return render_template('documentation/work.html')

@app.route('/vote')
def vote():
    return render_template('documentation/vote.html')

@app.route('/youtube')
def youtube():
    return render_template('documentation/youtube.html')
    
if __name__ == "__main__":
   app.run(debug=True)

def run():
   app.run(host='0.0.0.0',port=8080)

def keep_alive():
     t = Thread(target=run)
     t.start()

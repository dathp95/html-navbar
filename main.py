from flask import Flask, redirect, url_for,render_template

#Khởi tạo Flask server backend
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('home.html',title ='HOME')

@app.route("/<name>")
def user(name):
  return f'Hi {name}'

@app.route('/admin')
def admin():
  return redirect(url_for("hello"))

#Start backend
if __name__=='__main__':  
  app.run(host='0.0.0.0',port=9999,debug=True)
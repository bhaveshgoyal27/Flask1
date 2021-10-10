from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "goyal"
app.permanent_session_lifetime = timedelta(days=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'#Name of the table is users
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class users(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name =db.Column("name", db.String(100))
	email =db.Column("email", db.String(100))

	def __init__(self,name,email):
		self.name = name
		self.email = email

@app.route("/")
def home():
	return render_template("index2.html")

@app.route("/login", methods=["POST","GET"])
def login():
	if request.method =="POST":
		session.permanent = True#default is False
		user = request.form["name"]#name attribute of the input 
		session["user"] = user
		flash("Login sucessful!!")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already logged in!!")
			return redirect(url_for("user"))
	return render_template("login.html")

@app.route("/user", methods=["POST","GET"])
def user():
	email=None
	if "user" in session:
		user = session["user"]
		if request.method=="POST":
			email = request.form["email"]
			session["email"]=email
			flash("Email was saved!!")
		else:
			if "email" in session:
				email = session["email"]
		return render_template("user.html", user=user, email=email)
	else:
		flash("Please login!!")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash("You have been logged out{}".format(user), "info")
		session.pop("user",None)
		session.pop("email",None)
	return redirect(url_for("login"))


if __name__=="__main__":
	db.create_all()
	app.run(debug=True)
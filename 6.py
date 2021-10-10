from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "goyal"
app.permanent_session_lifetime = timedelta(days=5)

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

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return render_template("user.html", user=user)
	else:
		flash("Please login!!")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash("You have been logged out{}".format(user), "info")
		session.pop("user",None)
	return redirect(url_for("login"))


if __name__=="__main__":
	app.run(debug=True)
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index2.html")

@app.route("/login", methods=["POST","GET"])
def login():
	if request.method =="POST":
		user = request.form["name"]#name attribute of the input 
		return redirect(url_for("user",usr=user))
	return render_template("login.html")

@app.route("/<usr>")
def user(usr):
	return f"<h2>{usr}</h2>"


if __name__=="__main__":
	app.run(debug=True)
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return "This is the main page!!<br><h1>HELLO</h1>"

@app.route("/<name>")
def namer(name):
	return f"Hello {name}!!"

@app.route("/admin")
def admin():
	return redirect(url_for("namer", name="bhavesh"))
	return redirect(url_for("home"))

if __name__=="__main__":
	app.run(debug=True)
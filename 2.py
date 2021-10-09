from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
@app.route("/")
def home(name=None):
	#return render_template("index.html",content=name)
	l=["bhavesh", "goyal","dsvs"]
	return render_template("index.html",content=name, l=l)#multiple paramaters can be passed
	return "This is the main page!!<br><h1>HELLO</h1>"


if __name__=="__main__":
	app.run(debug=True)
from flask import Flask,Blueprint,render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second.route("/")
@second.route("/home")
def home():
	return render_template("home.html")

@second.route("/test")
def test():
	return "<h1>TESTING PAGE FOR Blueprint</h1>"
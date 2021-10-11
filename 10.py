from flask import Flask, redirect, url_for, render_template
from second import second

app = Flask(__name__)
app.register_blueprint(second,url_prefix="/second")


@app.route("/")
@app.route("/home")
def home():
	return "<h1>TESTING</h1>"

if __name__=="__main__":
	app.run(debug=True)
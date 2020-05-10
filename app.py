from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
	content = {"msg" : "hello"}
	return render_template('home.html', content=content)


if __name__ == '__main__':
    app.run(debug=True)
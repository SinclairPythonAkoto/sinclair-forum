from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)

@app.route('/')
def homepage():
	foot = "Design. Build. Apply!"
	return render_template('homepage.html', foot=foot)

if __name__ == '__main__':
	app.run()

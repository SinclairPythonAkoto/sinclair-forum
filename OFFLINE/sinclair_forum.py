from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)

@app.route('/')
def homepage():
	return 'hello Sinclair !'

if __name__ == '__main__':
	app.run()
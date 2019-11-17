from flask import Flask, render_template, url_for, request, flash, redirect
from db_table import * # this is a Python file of database tables

app = Flask(__name__)

Session = sessionmaker(bind=engine)
db_session = Session()

foot = "Design. Build. Apply!"

@app.route('/')
def homepage():
	title = "Sinclair's Forum"
	return render_template('homepage.html', foot=foot)

@app.route('/view_db')
def view_db:
	title = "View Database"
	data = db_session.query(SinTest).order_by(SinTest.id).all()
	return render_template('view_db.html', title=title, foot=foot, data=data)



if __name__ == '__main__':
	app.run()

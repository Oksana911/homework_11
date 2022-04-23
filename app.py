import utils

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main_page():
	name = "Ivan"

	return render_template('list.html', name=name)


app.run()


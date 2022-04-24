from flask import Flask, render_template


app = Flask(__name__)


@app.route('/',)
def page_index():

    return render_template("cat_profile.html")


app.run(port=2345)
from flask import Flask, render_template

from analytics.critical_power.power import power

app = Flask(__name__, template_folder='www/templates', static_folder='www/assets')

@app.route("/")
@app.route("/power")
def athlete_power():
    return render_template("power.html", msg="Hello world")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

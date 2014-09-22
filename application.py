from flask import Flask, render_template, jsonify, request

from analytics.critical_power.power import power

app = Flask(__name__, template_folder='www/templates', static_folder='www/assets')

@app.route("/")
@app.route("/power")
def athlete_power():
    return render_template("power.html", msg="Hello world")

@app.route("/calculate", methods=['POST'])
def calculate_power():
    print request.form

    if request.form:

        try:
            distance  = float(request.form['distance'])
            time      = float(request.form['time'])
            angle     = float(request.form['angle'])
            height    = float(request.form['height'])
            mass      = float(request.form['mass'])
            temp      = float(request.form['temperature'])
            elevation = float(request.form['elevation'])

            result = round(power(distance, time, angle, height, mass, temp, elevation), 3)
        except Exception as e:
            print e
            return jsonify(success=False, result="Failed to calculate power. Make sure inputs are correct")

        return jsonify(success=True, result=result)

    return jsonify(success=False, result="Failed to calculate power. Make sure inputs are correct")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from flask import flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calc",methods=['GET','POST'])
def calculation():
    if request.method  == "GET":
        return render_template('calculation.html')
    elif request.method == "POST":
        top = request.form['top']
        bottom = request.form['bottom']
        height = request.form['height']
        # 台形の計算
        answer = trapezoid_area(top, bottom, height)

        return render_template('calculation.html', result=answer)

if __name__ == "__main__":
    app.run(debug=True)

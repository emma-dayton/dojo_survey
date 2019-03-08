from flask import Flask, render_template, request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    # location = request.form['location']
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

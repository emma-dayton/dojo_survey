from flask import Flask, render_template, request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    location = request.form.get('location')
    language = request.form.get('language')
    comment = request.form['comment']

    return render_template("index.html", name=name, location=location, language=language, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)

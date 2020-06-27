from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# http methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST METHOD'
    else:
        return 'GET METHOD'


if __name__ == "__main__":
    app.run(debug=True)

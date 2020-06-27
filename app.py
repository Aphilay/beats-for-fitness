from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playlist.db'
db = SQLAlchemy(app)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(20), nullable=False)
    bpm = db.Column(db.Integer, nullable=False, default='N/A')

    def __repr__(self):
        return 'Song  ' + str(self.id)


# dummy data
my_playlist = [
    {
        'artist': 'Drake',
        'song': 'Pain 1993'
    },
    {
        'artist': 'Future',
        'song': 'Outer Space Bih'
    }
]


@app.route('/')
def index():
    return render_template('index.html')

# playlists is the keyword used in the for loop in playlist.html
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/playlist', methods=['GET', 'POST'])
def playlist():
    return render_template('playlist.html', playlists=my_playlist)


# http methods example
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST METHOD'
    else:
        return 'GET METHOD'


if __name__ == "__main__":
    app.run(debug=True)

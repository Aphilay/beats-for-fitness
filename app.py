from flask import Flask, request, render_template, redirect
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


@app.route('/')
def index():
    return render_template('index.html')

# playlists is the keyword used in the for loop in playlist.html
@app.route('/about')
def about():
    return render_template('about.html')

# GET: retrives the playlist stored in db
# POST: takes form data in playlist.html and stores in db
@app.route('/playlist', methods=['GET', 'POST'])
def playlist():
    if request.method == 'POST':
        song_title = request.form['title']
        artist = request.form['artist']
        bpm = request.form['bpm']
        new_song = Song(title=song_title, artist=artist, bpm=bpm)
        db.session.add(new_song)
        db.session.commit()
        return redirect('/playlist')
    else:
        all_songs = Song.query.order_by(Song.id).all()
        return render_template('playlist.html', playlist=all_songs)


@app.route('/playlist/delete/<int:id>')
def delete(id):
    song = Song.query.get_or_404(id)
    db.session.delete(song)
    db.session.commit()
    return redirect('/playlist')


@app.route('/playlist/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    song = Song.query.get_or_404(id)

    if request.method == 'POST':
        song.title = request.form['title']
        song.artist = request.form['artist']
        song.bpm = request.form['bpm']
        db.session.commit()
        return redirect('/playlist')
    else:
        # keyword post allows edit.html to get access to song obj
        return render_template('edit.html', song=song)


if __name__ == "__main__":
    app.run(debug=True)

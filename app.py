from flask import Flask, request, render_template


app = Flask(__name__)

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


@app.route('/playlist')
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

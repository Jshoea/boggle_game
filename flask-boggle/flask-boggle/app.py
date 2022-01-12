from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session
boggle_game = Boggle()

app= Flask(__name__)
app.config["SECRET KEY"] = "secretKey"

@app.route("/")
def homepage():
    """Will display the main board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("index.html", board=board, highscore=highscore, nplays=nplays)

@app.route("/check-word")
def check_word():
    """Check words in dictionary words.txt"""

    word = request.args["words"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/post-score", methods=["POST"])
def post_score():
    """grabs the score, and updates the nplay then will update score if its highscore"""
    score = request.json["score"]

    highscore = session.get("highscore", 0)

    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(breakRecord = score > highscore)



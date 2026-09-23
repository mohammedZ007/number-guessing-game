from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

# Required for Flask sessions
app.secret_key = "number-guessing-game-secret-key"


@app.route("/", methods=["GET", "POST"])
def game():

    # Start a new game if no game exists
    if "number" not in session:
        session["number"] = random.randint(1, 10)
        session["chances"] = 3
        session["message"] = "I have chosen a number between 1 and 10."

    if request.method == "POST":

        # Don't accept guesses after game is over
        if session["chances"] <= 0:
            session["message"] = "Game Over! Click New Game to play again."
            return render_template("index.html")

        try:
            guess = int(request.form["guess"])

            # Validate input
            if guess < 1 or guess > 10:
                session["message"] = "Please enter a number between 1 and 10."
                return render_template("index.html")

            # Consume one chance
            session["chances"] -= 1

            # Correct guess
            if guess == session["number"]:
                session["message"] = (
                    "Congratulations! You guessed correctly! 🎉"
                )

            # Near guess
            elif abs(session["number"] - guess) <= 2:
                session["message"] = "You are near! Try again."

            # Far guess
            else:
                session["message"] = "You are far away! Try again."

            # Game over
            if session["chances"] == 0 and guess != session["number"]:
                session["message"] = (
                    f"Game Over! The correct number was {session['number']}."
                )

        except (ValueError, TypeError):
            session["message"] = "Please enter a valid number."

    return render_template("index.html")


@app.route("/new-game", methods=["GET", "POST"])
def new_game():

    # Completely reset the previous game
    session.clear()

    # Create a fresh game
    session["number"] = random.randint(1, 10)
    session["chances"] = 3
    session["message"] = "I have chosen a number between 1 and 10."

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

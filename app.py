import random
from flask import Flask, render_template, request, session, redirect
from questions import questions

app = Flask(__name__)
app.secret_key = "apcsppractice"

QUESTION_BANKS = {
    "1": {
        "easy": questions.bigidea1_easy,
        "medium": questions.bigidea1_medium,
        "hard": questions.bigidea1_hard,
        "challenge": questions.bigidea1_challenge,
    },

    "2": {
        "easy": questions.bigidea2_easy,
        "medium": questions.bigidea2_medium,
        "hard": questions.bigidea2_hard,
        "challenge": questions.bigidea2_challenge,
    },

    "3": {
        "easy": questions.bigidea3_easy,
        "medium": questions.bigidea3_medium,
        "hard": questions.bigidea3_hard,
        "challenge": questions.bigidea3_challenge,
    },

    "4": {
        "easy": questions.bigidea4_easy,
        "medium": questions.bigidea4_medium,
        "hard": questions.bigidea4_hard,
        "challenge": questions.bigidea4_challenge,
    },

    "5": {
        "easy": questions.bigidea5_easy,
        "medium": questions.bigidea5_medium,
        "hard": questions.bigidea5_hard,
        "challenge": questions.bigidea5_challenge,
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question")
def question():
    return "You reached the question route!"


@app.route("/bigidea")
def bigidea():
    return render_template("bigidea.html")


@app.route("/practice")
def practice():
    bigidea = request.args.get("bigidea")

    return render_template(
        "practice_mode.html",
        bigidea=bigidea
    )


@app.route("/difficulty")
def difficulty():
    bigidea = request.args.get("bigidea")

    return render_template(
        "difficulty.html",
        bigidea=bigidea
    )


@app.route("/questions")
def quiz():
    bigidea = request.args.get("bigidea")
    difficulty = request.args.get("difficulty")
    mode = request.args.get("mode")

    if mode == "progressive" and difficulty is None:
        difficulty = "easy"

    question_bank = QUESTION_BANKS[bigidea][difficulty]

    if difficulty == "challenge":
        amount = 20
    else:
        amount = 10

    quiz = random.sample(question_bank, amount)

    session["quiz"] = quiz
    session["current"] = 0
    session["score"] = 0
    session["mode"] = mode
    session["difficulty"] = difficulty
    session["bigidea"] = bigidea

    return render_template(
        "question.html",
        question=quiz[0],
        number=1,
        total=amount
    )


@app.route("/retry")
def retry():
    return render_template("retry.html")


@app.route("/answer", methods=["POST"])
def answer():
    user_answer = request.form.get("answer")

    current = session["current"]

    question = session["quiz"][current]

    if user_answer == question["answer"]:
        correct = True
        session["score"] += 1
    else:
        correct = False

    return render_template(
        "answer.html",
        correct=correct,
        question=question
    )


@app.route("/next")
def next_question():
    session["current"] += 1

    current = session["current"]

    quiz = session["quiz"]

    if current >= len(quiz):
        return redirect("/results")

    return render_template(
        "question.html",
        question=quiz[current],
        number=current + 1,
        total=len(quiz)
    )


@app.route("/results")
def results():
    score = session["score"]
    total = len(session["quiz"])
    mode = session["mode"]
    difficulty = session["difficulty"]
    bigidea = session["bigidea"]

    passed = score >= 8

    if difficulty == "easy":
        next_difficulty = "medium"

    elif difficulty == "medium":
        next_difficulty = "hard"

    elif difficulty == "hard":
        next_difficulty = "challenge"

    else:
        next_difficulty = None

    # Progressive Mode is completely finished!
    if mode == "progressive" and difficulty == "challenge" and passed:
        return render_template(
            "finished.html",
            bigidea=bigidea
        )

    return render_template(
        "results.html",
        score=score,
        total=total,
        mode=mode,
        difficulty=difficulty,
        bigidea=bigidea,
        passed=passed,
        next_difficulty=next_difficulty
    )


if __name__ == "__main__":
    app.run(debug=True)
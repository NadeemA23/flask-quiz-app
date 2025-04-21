from flask import Flask, render_template, request
import random
from questions import quiz_questions

app = Flask(__name__)

@app.route('/')
def quiz():
    return render_template("index.html", questions=quiz_questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in quiz_questions:
        user_answer = request.form.get(question['question'])
        if user_answer == question['answer']:
            score += 1
    return render_template("result.html", score=score, total=len(quiz_questions))

if __name__ == "__main__":
    app.run(debug=True)
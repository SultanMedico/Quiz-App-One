from flask import Flask, render_template, request

app = Flask(__name__)

QUESTIONS = [
    {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is the largest ocean?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Austen", "Tolkien"], "answer": "Shakespeare"},
    {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "What is H2O?", "options": ["Oxygen", "Hydrogen", "Salt", "Water"], "answer": "Water"},
    {"question": "Which country invented pizza?", "options": ["USA", "India", "Italy", "China"], "answer": "Italy"},
    {"question": "Who painted the Mona Lisa?", "options": ["Van Gogh", "Picasso", "Da Vinci", "Rembrandt"], "answer": "Da Vinci"}
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answers = request.form
        score = 0
        for i, q in enumerate(QUESTIONS):
            if user_answers.get(f'q{i}') == q['answer']:
                score += 1
        return render_template("index.html", questions=QUESTIONS, submitted=True, score=score)
    return render_template("index.html", questions=QUESTIONS, submitted=False)

if __name__ == "__main__":
    app.run(debug=True)

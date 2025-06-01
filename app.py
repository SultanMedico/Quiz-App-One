from flask import Flask, render_template, request

app = Flask(__name__)

QUESTIONS = [
{"question": "OOP ka pura naam kya hai?", "options": ["Object-Oriented Programming", "Object-Oriented Protocol", "Object-Oriented Process", "Object-Oriented Paradigm"], "answer": "Object-Oriented Programming"},
{"question": "OOP mein 'Class' kya hai?", "options": ["Ek function ka naam", "Ek blueprint ya template jisse objects banaye jaate hain", "Ek variable ka type", "Ek data structure"], "answer": "Ek blueprint ya template jisse objects banaye jaate hain"},
{"question": "'Object' kya hai OOP mein?", "options": ["Class ki ek instance", "Ek variable ka naam", "Ek method ka naam", "Ek data type"], "answer": "Class ki ek instance"},
{"question": "Encapsulation ka kya matlab hai OOP mein?", "options": ["Data aur methods ko ek unit mein band karna", "Code ko dobara istemal karna", "Alag-alag classes mein inheritance karna", "Classes ke beech communication"], "answer": "Data aur methods ko ek unit mein band karna"},
{"question": "Inheritance ka kya maqsad hai OOP mein?", "options": ["Code ko hide karna", "Classes ke beech naye rishte banana", "Ek class ko dusri class ki properties aur methods virasat mein dena", "Bina kisi dependency ke code likhna"], "answer": "Ek class ko dusri class ki properties aur methods virasat mein dena"},
{"question": "Polymorphism ka kya matlab hai OOP mein?", "options": ["Ek hi naam ke functions ka alag-alag tarike se kaam karna", "Ek se zyada classes banana", "Ek hi object ka kai roop lena", "Data ko encrypt karna"], "answer": "Ek hi naam ke functions ka alag-alag tarike se kaam karna"},
{"question": "Abstraction kya hai OOP mein?", "options": ["Zaruri details ko dikhana aur ghair-zaruri ko chupana", "Pura code dikhana", "Sirf data ko hide karna", "Methods ko rename karna"], "answer": "Zaruri details ko dikhana aur ghair-zaruri ko chupana"},
{"question": "OOP mein 'Constructor' ka kya kaam hai?", "options": ["Object ko destroy karna", "Object ko initialize karna", "Method ko call karna", "Variable ko declare karna"], "answer": "Object ko initialize karna"},
{"question": "OOP mein 'Method Overloading' kya hai?", "options": ["Ek hi class mein ek hi naam ke kai methods ka hona, lekin alag-alag parameters ke saath", "Ek method ka dusri class mein dobara istemal", "Ek method ko override karna", "Ek method ka naam badalna"], "answer": "Ek hi class mein ek hi naam ke kai methods ka hona, lekin alag-alag parameters ke saath"},
{"question": "OOP mein 'Method Overriding' kya hai?", "options": ["Parent class ke method ko child class mein dobara define karna", "Ek method ko delete karna", "Ek method ko naya naam dena", "Ek method ko private banana"], "answer": "Parent class ke method ko child class mein dobara define karna"}
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

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = list()


for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

q1 = QuizBrain(question_bank)

while q1.still_has_questions():
    q1.next_question()

print("You've completed the quiz")
print(f"Your final score was: {q1.score}/{q1.question_number}")
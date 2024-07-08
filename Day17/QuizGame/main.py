from Day17.QuizGame import quiz_brain
from data import question_data
from questions import Question
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
quiz_brain=QuizBrain(question_bank)
while quiz_brain.has_question():
    quiz_brain.next_question()

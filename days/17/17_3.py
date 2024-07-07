from question_model import Question
from data import question_data
from quiz_brain import Quiz
import random

question_bank = []

for each in question_data:
    question_bank.append(Question(each["text"], each["answer"]))
    
random.shuffle(question_bank)

quiz = Quiz()

to_continue = True

while to_continue:
    
    # ask_question has been added to the check_answer function
    quiz.check_answer(question_bank)
    if(quiz.end_reached(question_bank)):
        to_continue = False
    
    

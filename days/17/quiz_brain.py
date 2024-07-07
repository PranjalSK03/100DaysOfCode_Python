class Quiz:
    def __init__(self):
        self._correct_answer = 0
        self._question_asked = 0
        
    def _ask_question(self, text):
        answer = input(f"\n{text.question}? (True/False): ") # pass text type "Question"
        return answer
    
    def check_answer(self, text_arr):        
        if(text_arr[self._correct_answer-1].answer.lower() == self._ask_question(text_arr[self._correct_answer-1]).lower().replace(" ",  "")):
            self._correct_answer +=1
            self._question_asked +=1 
        else:
            self._question_asked +=1 
            
        print(f"The correct answer was: {text_arr[self._correct_answer-2].answer} ")
        print(f"Your current score is: ({self._correct_answer}/{self._question_asked})")
        
    def end_reached(self, text_arr):
        if(self._correct_answer < self._question_asked):
            return True
        if(len(text_arr) == self._correct_answer):
            print("\nYou have successfully completed the quiz !!🎉🎊")
            return True
        
        return False
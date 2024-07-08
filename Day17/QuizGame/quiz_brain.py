class QuizBrain:
    def __init__(self, q_list):
        self.q_list=q_list
        self.question_number=0
        self.score=0
    def next_question(self):
        current_question=self.q_list[self.question_number]
        answer=input(f"Q{self.question_number+1}: {current_question.text}. True/False")
        correct_answer=current_question.answer
        self.check_answer(answer,correct_answer)
        self.question_number+=1
    def has_question(self):
        return self.question_number<len(self.q_list)
    def check_answer(self, answer,correct_answer):
        if answer.lower()==correct_answer.lower():
            print("YOU RİGHT")
            self.score+=1
        else:
            print("WRONG ")
        print(f"{self.score}/{self.question_number + 1}")
        print("**********************************************")
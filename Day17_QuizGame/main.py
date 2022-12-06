# class User:
#     def __init__(self,id,username):
#         self.id=id
#         self.username=username
#         self.followers=0 #providing a default value
#         self.following=0
#         print("New user being created...")
#     def follow(self,user): #a method always needs a self parameter
#         user.followers +=1
#         self.following +=1

# user1=User("001",'angela') 
# user2=User("002", "Jack")
# user1.follow(user2)
# print(user1.followers,user1.following,user2.followers,user2.following)


from types import new_class
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for question in question_data:
    new_question=Question(question["text"], question["answer"])
    question_bank.append(new_question)
    
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Final score: {quiz.score}/{quiz.question_number}")
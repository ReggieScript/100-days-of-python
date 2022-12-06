import art
import game_data as gd
import random
import os

# Generate a random number and a random person from the data

def obtain_data():
    x=random.choice(gd.data)
    return x
#compare follower counts

def compare(z,y):
    if z['follower_count'] > y['follower_count']:
        return 1
    else:
        return 2

def higher_lower(a,b,score,cont):
    print(art.logo)
    if score>0:
        print(f"You're right! Your score is {score}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    choice=input("Who has more followers? Type 'A' or 'B':\n")
    choicecomp=compare(a,b)
    os.system('cls')
    if (choicecomp== 1 and choice=='A') or (choicecomp== 2 and choice=='B'):
        score=score+1
    else:  
        cont=0
    return score, cont

x=0
cont=1
a=obtain_data()
b=obtain_data()
while cont ==1:
    while a==b:
        b=random.choice(gd.data)
    func=higher_lower(a,b,x,cont)
    cont=func[1]
    x=func[0]
    a=b
    b=obtain_data()
print(art.logo)
print(f"Sorry, that's wrong. Final score: {x}")
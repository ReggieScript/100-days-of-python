

#Dictionary Exercise

# student_scores = {
#     "Harry":81,
#     "Ron": 78,
#     "Hermionie": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades={}

# for key in student_scores:
#     if student_scores[key]>=91:
#         student_grades[key]="Outstanding"
#     elif student_scores[key]>=81:
#         student_grades[key]="Exceeds Expectations"
#     elif student_scores[key]>=71:
#         student_grades[key]="Acceptable"
#     elif student_scores[key]<70:
#         student_grades[key]="Fail"

# print(student_grades)

#Secret Auction program

import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Welcome to the secret auction program.")

cont="yes"

secret_auction={
    "name":[],
    "bid": [],
}

names=[]
bids=[]

while cont == "yes":
    name=input("What is your name?\n")
    bid=input("What is your bid?\n")
    cont=input("Are there any other bidders? Type 'yes' or 'no'\n")
    names.append(name)
    bids.append(int(bid))
    os.system('cls')

secret_auction["name"]=names
secret_auction["bid"]=bids

index_max= secret_auction["bid"].index(max(secret_auction["bid"]))

print("The winner is {} with a bid of ${}.".format(secret_auction["name"][index_max],secret_auction["bid"][index_max]))
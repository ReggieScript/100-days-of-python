import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nm_letters=int(input("How many letters would you like in your password?\n"))
nm_symb=int(input("How many symbols would you like\n"))
nm_num=int(input("How many numbers would you like?\n"))

total=nm_letters+nm_symb+nm_num

pswd=""
chars=range(0,total)
while total !=0:
    rand=random.randint(0,2)
    if rand==0:
        if nm_letters !=0:
            pswd=pswd+str(letters[random.randint(0,51)])
            nm_letters=nm_letters-1
            total=total-1
    if rand==1:
        if nm_symb !=0:
            pswd=pswd+str(symbols[random.randint(0,8)])
            nm_symb=nm_symb-1
            total=total-1
    if rand==2:
        if nm_num != 0:
            pswd=pswd+str(numbers[random.randint(0,9)])
            nm_num=nm_num-1
            total=total-1

print("Your password is: "+pswd)
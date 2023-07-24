import random
import hangman_words as wrds
import hangman_art as art
import os

lives=6 #variable de vidas

#Bienvenida al jugador

print("Welcome to")
print(art.logo)

chosen_word = wrds.word_list[random.randint(0,len(wrds.word_list))]

blank=[]
for i in chosen_word:
  blank.append("_")

guesses=[]  #variable para ir agregando las letras usadas

while (chosen_word !=''.join(blank) and lives>=0):
  guess=input("Guess a letter:\n").lower()
  os.system('clear')
  if guess in chosen_word:
    for i in range(0,len((chosen_word))):
      if chosen_word[i]==guess:
        blank[i]=guess
    print(art.stages[lives])
    print("You got a guess!")
    print(''.join(blank))
  if guess not in chosen_word:
      lives=lives-1
      print(art.stages[lives])
      print("Wrong guess. Try Again")
      print(''.join(blank))
  guesses.append(guess)
  guesses.append(" ")
  print("Letters used: "+ ''.join(guesses))

if chosen_word == ''.join(blank):
  print("You won!")
else:
  print("You lost :(")
  print("The correct word was: "+ chosen_word)
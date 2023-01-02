import pandas

#TODO 1. Create a dictionary in this format:

nato_df=pandas.read_csv(r"Day26_NatoAlphabet\nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index,row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word=input("Enter a word").strip()

code_word=[nato_dict[letter.capitalize()] for letter in input_word]
print(code_word)
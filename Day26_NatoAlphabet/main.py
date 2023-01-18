import pandas


nato_df=pandas.read_csv(r"Day26_NatoAlphabet\nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index,row) in nato_df.iterrows()}


while True:
    input_word=input("Enter a word:").strip()
    try:
        code_word=[nato_dict[letter.capitalize()] for letter in input_word] 
    except KeyError:
        print("Sorry, letters only")
    else:
        print(', '.join(str(word)for word in code_word))
        break
    
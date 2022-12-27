letter = open(r"Day24_MailMerger\Input\Letters\starting_letter.txt", "r")
names = open(r"Day24_MailMerger\Input\Names\invited_names.txt", "r")

letter_lines = letter.readlines()
name_lines = names.readlines()


for name in name_lines:
    name = name.strip()  # We need to remove any extra spaces on the name for this to work
    # file directory for the file, if it exits it will just overwrite it
    letter_file = open(f"Day24_MailMerger\Output\ReadyToSend\letter_for_{name}", "w")
    new_letter = letter_lines[0] #just the first line of the letter
    full_letter = letter_lines[1:] #the rest of the letter
    new_letter = new_letter.replace("[name]", name)
    full_letter.insert(0, new_letter)
    for line in full_letter:
        letter_file.write(line)
    letter_file.close()

letter.close()
names.close()
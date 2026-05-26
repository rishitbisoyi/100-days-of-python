#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("24_Files/MailMerge/Input/Letters/starting_letter.txt") as letter_f:
    letter_contents = letter_f.read()


with open("24_Files/MailMerge/Input/Names/invited_names.txt") as names_f:
    names = names_f.readlines()


for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace("[name]", stripped_name)
    with open(f"24_Files/MailMerge/Output/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
        completed_letter.write(new_letter)
print("Please type the name of the file you would like to open:")
txt = input("> ")
txt_again = open(txt)
#prints out text that states that it is opening your file.
print(f"Here is your file {txt}:")
#prints out the text from the file
print(txt_again.read())
txt_again.close()

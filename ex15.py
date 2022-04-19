
#imports modules from the sys package
from sys import argv
#unpacks argv
script, filename = argv
#sets variabls "txt" to the function open and it opens the file.
txt = open(filename)
#prints out text that states that it is opening your file.
print(f"Here is your file {filename}:")
#prints out the text from the file
print(txt.read())
#prints text prompting you to type the file name in again.
print("Type the filename again: ")
#prompts an imput from the user to type the file name in again, and also uses the input function to set the variable file_again
file_again = input("> ")
#sets the variable text_again and uses the open function to open the file defined by the variable file_again
txt_again = open(file_again)
#prints out the file that was defined by the variable text_again
print(txt_again.read())
txt.close()
txt_again.close()

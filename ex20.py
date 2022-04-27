#imports commands
from sys import argv
#unpacks argv
script, input_file = argv
#sets the function print_all
def print_all(f):
    print(f.read())
#sets the function rewind which in this case sets the file back at the first byte
def rewind(f):
    f.seek(0)
#defines the funtion print a line and sets the variables to line_count and f
def print_a_line(line_count, f):
    print(line_count, f.readline())
#sets the variable current_file to open the input file from the start
current_file = open(input_file)

print("Let's print the whole file:\n")
#calls the function print_all and sets the variable f to the current file which opens the input file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
#calls the function rewind and sets the variable to the current_file
rewind(current_file)

print("Let's print 3 lines:")
#sets the current_line variable to 1
current_line = 1
#calls the function print_a_line, and sets the function variables to current_line (Which is equal to 1 in this case), and current_file
print_a_line(current_line, current_file)
#bumps the current_line variable up by 1
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

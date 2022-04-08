#creates a string of a variable named formatter
formatter = "{} {} {} {}"
#assigns a value to the variable formatter and formats it to be printed
print(formatter.format(1, 2, 3, 4))


#testing to see if I know whats happening
test = "{} {} {} {}"
#result
print(test.format("W", "I", "L", "L"))

smart = True

print(f"Will is smart? {smart}")

#Back to the excercise
print(formatter.format("one", "two", "three", "four."))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"I love my son,",
"he is the best,",
"he is like me,",
"but small."))

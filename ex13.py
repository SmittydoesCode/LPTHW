from sys import argv

script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is called", first)
print("Your second variable is called", second)
print("Your third variable is called", third)

print("********************************************")
print("\nHere is a study drill.")

input("Knock, Knock ")
input("Boo ")
print("Why are you crying?")

hilarious = False
joke_evaluation = "Wasn't that joke so funny?!?! {}"
print(joke_evaluation.format(hilarious))
input("Why are you so mean?")
print("Here is some math...")
print("If x = 3 * 3\n Solve for x")
y = int(input("x = ? "))
x = 9
print(f"You said {y}, x = {x}")

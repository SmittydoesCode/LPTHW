def study_drill(fun_level, bored_level):
    print(f"You are having {fun_level}-10 amount of fun!")
    print(f"You are {bored_level} bored!")

print("Please enter your fun level on a scale of 1-10.")
fun = input("> ")

print("Please enter your boredom percentage.")
bored = input("> ")

study_drill(fun, bored)

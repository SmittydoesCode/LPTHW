#defines function cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("Thats enough for a party!\nGrab a blanket\n")

#shows how to give the function variables value directly
print("We can just give the numbers directly.")
cheese_and_crackers(10,15)
#Uses the variables from the script to set the values of the function
print("Or, we can use variables from the script!")
amount_of_cheese = 10
amount_of_crackers = 15

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#demonstrates the abillity to do math inside to set the variables within the function
print("We can even do math inside too:")
cheese_and_crackers(5+5,10+5)
#combines the script variables and math to set the values for the function
print("And we can combine the two: variables and math!")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

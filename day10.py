print("tip calculator")
bill = float(input("how much was the total bill? > "))
percent = float(input("what percent of the total amount would you like to tip? > ")) / 100
total = round(percent * bill, 2) + bill
print(total)
numPeople = float(input("how many people are splitting the bill? > "))
final = round(total / numPeople, 2)
print(final)
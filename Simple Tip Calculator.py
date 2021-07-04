#Simple Tip Calculator
print("Welcome to the Simple tip Calculator!")
money = float(input("what was the total bill amount?  $ "))
tip = int(input("how much percentage of tip would you like to give?"))
people = int(input("how many people to split the bill?"))
tip_as_per= tip / 100 
total_tip_amount = money * tip_as_per
total_bill = money + total_tip_amount
bill_per_person = total_bill / people
#round the result to 2 decimal places
final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount} INR ")
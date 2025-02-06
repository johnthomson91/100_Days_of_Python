print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

def total_per_person(bill, tip, people):
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    return bill_per_person

final_amount = round(total_per_person(bill, tip, people), 2)

print(f"Each person should pay: ${final_amount}")



print("Welcome to the tip calculator!")

# User input
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15: "))
people = int(input("How many people to split the bill? "))

# Calculate total tip and amount per person
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
amount_per_person = round(total_bill / people, 2)

# Output result
print(f"Each person should pay: ${amount_per_person}")
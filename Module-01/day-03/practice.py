#IN-CLASS EXERCISES-TRANSACTION LOG READER

# Read a file of TeleBirr transactions, summarise them by customer using a dictionary, and handle a missing file gracefully.
import os
import sys
def read_transactions(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    transactions = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 3:
                print(f"Skipping malformed line: {line.strip()}")
                continue
            customer_id, transaction_type, amount = parts
            try:
                amount = float(amount)
            except ValueError:
                print(f"Invalid amount '{amount}' for customer '{customer_id}'. Skipping.")
                continue

            if customer_id not in transactions:
                transactions[customer_id] = {'total': 0, 'count': 0}
            transactions[customer_id]['total'] += amount
            transactions[customer_id]['count'] += 1

    return transactions


######## PRACICE EXERCISES ####




# #1. Unique cities. Given a list with repeated city names, use a set to print the distinct cities, then the count.

cities = ["Addis", "Dire Dawa", "Bahir Dar", "Adama", "Shaggar", "Shaggar"]
unique=set(cities)
print(unique)
print(len(unique))




# #2. Price report. Make a dictionary of five grocery items and prices in ETB. Loop with .items() to print each on its own line.

grocery={"Rice": 150, "Wheat": 200, "Barley": 180, "Corn": 120,
         "Oats": 140}
for item, price in grocery.items():
    print(f"{item}: {price} ETB")




# #3. Tax comprehension. Given prices = [100, 250, 400, 80], use one comprehension to build a list with 15% tax added.
prices = [100, 250, 400, 80]

taxed_prices = [price * 1.15 for price in prices]
print(taxed_prices)




# 4. Cheap items. From the same list, use a comprehension with a condition to keep only prices
# under 200.


prices = [150, 250, 99, 400, 185, 300, 50]
cheap_prices = [price for price in prices if price < 200]

print("Original prices:", prices)
print("Cheap prices (under 200):", cheap_prices)




# 5. Write & read. Write three customer names to names.txt, then open it and print each name
# back, one per line

with open("names.txt", "w") as file:
    file.write("Abdi\n")
    file.write("Sifan\n")
    file.write("Chala\n")

print("Names successfully written to names.txt.\n")

print("Reading names from file:")
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())





# 6. Safe division. Ask the user for a number and divide 1000 by it, catching both ValueError and
# ZeroDivisionError.

try:
    user_input = input("Enter a number to divide 1000 by: ")
    number = float(user_input)

    result = 1000 / number
    print(f"Success! 1000 divided by {number} is: {result}")

except ValueError:
    print("Error: Please enter a valid numerical value. Letters and symbols are not allowed.")

except ZeroDivisionError:
    print("Error: Division by zero is mathematically impossible. Please enter a number other than 0.")
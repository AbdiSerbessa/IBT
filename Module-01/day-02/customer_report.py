# 1. Store at least five customers as a list of (name, balance) pairs (tuples)
customers = [
    ("Abdi", 1250.00),
    ("Sifan", 850.50),
    ("Chala", 320.00),
    ("Marta", 1000.00),
    ("Tariku", 450.75)
]

# 2. Write a function to determine the customer's tier based on balance
def tier(balance):
    """
    Returns the customer tier based on their TeleBirr balance.
    - "Premium" for balance >= 1000 ETB
    - "Standard" for balance >= 500 ETB
    - "Basic" for balance below 500 ETB
    """
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"

# 3. Main program execution
def main():
    # Dictionaries to keep track of counts for each tier
    tier_counts = {
        "Premium": 0,
        "Standard": 0,
        "Basic": 0
    }
    
    print("==================================================")
    print("            TELEBIRR CUSTOMER REPORT              ")
    print("==================================================")
    # Header alignment: Left-aligned Name (12 spaces), Tier (12 spaces), Balance (Right-aligned, 10 spaces)
    print(f"{'Name':<12} | {'Tier':<12} | {'Balance':>10}")
    print("-" * 50)
    
    # Loop over the customers list
    for name, balance in customers:
        # Determine tier
        customer_tier = tier(balance)
        
        # Increment the corresponding tier count
        tier_counts[customer_tier] += 1
        
        # Print tidy line (formatting balance to 2 decimal places with 'ETB')
        balance_str = f"{balance:.2f} ETB"
        print(f"{name:<12} | {customer_tier:<12} | {balance_str:>10}")
        
    print("-" * 50)
    print("                SUMMARY REPORT                    ")
    print("-" * 50)
    # After the loop, print how many customers are in each tier
    for tier_name, count in tier_counts.items():
        print(f"Total {tier_name} Customers: {count}")
    print("==================================================")

if __name__ == "__main__":
    main()
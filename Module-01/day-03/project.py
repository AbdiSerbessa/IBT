import os

FILENAME = "stock.txt"

def load_stock(filename):
    """Loads stock from a comma-separated file into a dictionary."""
    stock_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                
                # Split item name and quantity by comma
                item, qty_str = line.split(',')
                stock_dict[item.strip()] = int(qty_str.strip())
        print(f"Successfully loaded stock from {filename}.")
    except FileNotFoundError:
        print(f"Warning: '{filename}' not found. Starting with an empty inventory.")
    except ValueError:
        print("Error: Found malformed data in stock file. Please check its formatting.")
    
    return stock_dict


def update_quantity(stock_dict, item, amount):
    """Increases or decreases an item's quantity by a given amount."""
    # Convert item to title case to match the dictionary keys consistently
    formatted_item = item.strip().title()
    
    if formatted_item in stock_dict:
        stock_dict[formatted_item] += amount
        # Ensure inventory doesn't drop below zero
        if stock_dict[formatted_item] < 0:
            stock_dict[formatted_item] = 0
        print(f"Updated {formatted_item}. New quantity: {stock_dict[formatted_item]}")
    else:
        # If the item doesn't exist and we're adding stock, create it
        if amount > 0:
            stock_dict[formatted_item] = amount
            print(f"Added new item: {formatted_item} with quantity {amount}")
        else:
            print(f"Error: Cannot decrease stock for '{formatted_item}' because it does not exist.")


def print_low_stock(stock_dict, threshold=10):
    """Uses a list comprehension to find and print low-stock items."""
    low_stock_items = [item for item, qty in stock_dict.items() if qty < threshold]
    
    print("\n--- Low Stock Report (Below 10) ---")
    if low_stock_items:
        for item in low_stock_items:
            print(f"⚠️ {item}: only {stock_dict[item]} left!")
    else:
        print("✅ All stock levels are healthy.")
    print("-----------------------------------\n")


def save_stock(filename, stock_dict):
    """Writes the updated dictionary back to the stock file."""
    try:
        with open(filename, 'w') as file:
            for item, qty in stock_dict.items():
                file.write(f"{item},{qty}\n")
        print(f"Saved changes back to {filename}.")
    except IOError:
        print(f"Error: Could not write to file {filename}.")


# --- Main Demonstration Program Flow ---
def main():
    # 1. Load the initial stock
    inventory = load_stock(FILENAME)
    print("Initial Inventory State:", inventory)
    
    # 2. Print initial low-stock items
    print_low_stock(inventory)
    
    # 3. Simulate some updates
    print("Performing transactions...")
    update_quantity(inventory, "Amoxicillin", 5)     # Increase Amoxicillin from 8 to 13
    update_quantity(inventory, "Paracetamol", -15)   # Decrease Paracetamol from 50 to 35
    update_quantity(inventory, "Metformin", -2)       # Decrease Metformin from 5 to 3
    update_quantity(inventory, "Amoxicillin", -1)     # Decrease Amoxicillin from 13 to 12
    update_quantity(inventory, "insulin", 15)         # Add a brand new item
    
    # 4. Show the updated low-stock items
    print_low_stock(inventory)
    
    # 5. Save the state back to the file
    save_stock(FILENAME, inventory)


if __name__ == "__main__":
    main()
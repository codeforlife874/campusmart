# Global list to store seller/renter details
sellers_lenders = []

def collect_seller_details():
    print("Welcome to Campus Mart - Sell or Rent Items!\n")
    
    # Ask the user if they want to Sell or Rent
    while True:
        action = input("Do you want to Sell or Rent an item? (Enter 'Sell' or 'Rent'): ").strip().lower()
        if action in ['sell', 'rent']:
            break
        else:
            print("Invalid choice. Please enter 'Sell' or 'Rent'.")
    
    # Collect basic product details
    product_name = input("Enter the product name: ")
    category = input("Enter the product category (e.g., Stationary, Books, Assignments,Question Paper): ")
    
    # Ensure the price is a valid number
    while True:
        try:
            price = float(input(f"Enter the product price (₹): "))
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value for price.")
    
    # Additional optional details
    description = input("Enter a brief description of the product (optional): ")
    contact_info = input("Enter your contact information (email or phone): ")

    # Append the details to the global list
    sellers_lenders.append({
        "action": action,
        "product_name": product_name,
        "category": category,
        "price": price,
        "description": description,
        "contact_info": contact_info
    })

    # Confirmation
    print("\nThank you! Your product details have been added to Campus Mart.")
    print(f"Here are the details you provided:\nAction: {'Sell' if action == 'sell' else 'Rent'}\n"
          f"Product Name: {product_name}\nCategory: {category}\nPrice: ₹{price}\n"
          f"Description: {description}\nContact Info: {contact_info}")


# Main function
if __name__ == "__main__":
    while True:
        collect_seller_details()
        cont = input("\nDo you want to add another item? (yes/no): ").strip().lower()
        if cont != "yes":
            break

    # Display all entries in sellers_append
    print("\nAll Seller/Renter Entries:")
    for seller in sellers_lenders:
        print(seller)

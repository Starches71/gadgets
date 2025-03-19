import os

def main():
    filename = "home.txt"  # Change file name to home.txt

    # Create the file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            pass  # Create an empty file

    # Read existing products
    with open(filename, "r") as file:
        existing_products = set(file.read().splitlines())  # Store existing products in a set

    print("Enter product names (type 'end' to finish):")

    new_products = set()

    while True:
        product_name = input().strip()

        if product_name.lower() == "end":
            break  # Stop when "end" is entered

        # Add product to the set (automatically removes duplicates)
        if product_name:
            new_products.add(product_name)

    # Combine old and new unique products
    all_products = existing_products.union(new_products)

    # Save the updated product list to home.txt
    with open(filename, "w") as file:
        for product in sorted(all_products):  # Sort for consistency
            file.write(product + "\n")

    print(f"\nTotal unique products: {len(all_products)}")
    print("Product names have been saved to 'home.txt'.")

if __name__ == "__main__":
    main()

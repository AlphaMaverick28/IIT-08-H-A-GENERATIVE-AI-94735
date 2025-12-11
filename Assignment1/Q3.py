import csv


filename = "products.csv"

category_input = input("Enter category to filter products (case-insensitive): ").strip().lower()

total_rows = 0
count_above_500 = 0
price_sum = 0
price_count = 0
total_quantity = 0
products_in_category = []

print("\n--- CSV Rows (Clean Format) ---")

with open(filename, newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_rows += 1

        
        print(f"Product ID: {row['product_id']} | "
              f"Name: {row['product_name']} | "
              f"Category: {row['category']} | "
              f"Price: {row['price']} | "
              f"Quantity: {row['quantity']}")

        
        price = float(row["price"])
        qty = int(row["quantity"])

        

        
        if price > 500:
            count_above_500 += 1

        
        price_sum += price
        price_count += 1

       
        if row["category"].strip().lower() == category_input:
            products_in_category.append(row["product_name"])

        
        total_quantity += qty


average_price = price_sum / price_count if price_count > 0 else 0


print("\n--- Summary ---")
print("Total rows:", total_rows)
print("Products priced above 500:", count_above_500)
print("Average price of all products:", round(average_price, 2))
print("Total quantity of all items in stock:", total_quantity)

print(f"\nProducts in category '{category_input}':")
if products_in_category:
    for p in products_in_category:
        print(" -", p)
else:
    print("No products found in this category.")

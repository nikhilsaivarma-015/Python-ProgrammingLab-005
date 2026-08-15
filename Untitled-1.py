# Smart Shopping Bill Generator
# Accepts customer and product details, applies a discount, and prints the bill
 
# Accept customer name
customer_name = input("Enter Customer Name: ")
 
# Accept names and prices of three products (type conversion: str -> float)
product1_name = input("Enter Product 1 Name: ")
product1_price = float(input(f"Enter Price of {product1_name}: "))
 
product2_name = input("Enter Product 2 Name: ")
product2_price = float(input(f"Enter Price of {product2_name}: "))
 
product3_name = input("Enter Product 3 Name: ")
product3_price = float(input(f"Enter Price of {product3_name}: "))
 
# Calculate total amount using the arithmetic (+) operator
total_amount = product1_price + product2_price + product3_price
 
# Apply a 10% discount if the total exceeds Rs. 3000
if total_amount > 3000:
    discount = total_amount * 0.10
else:
    discount = 0
 
# Calculate the final payable amount
final_amount = total_amount - discount
 
# Display the bill using f-strings
print("\n----------- SHOPPING BILL -----------")
print(f"Customer Name : {customer_name}")
print(f"{product1_name:<15}: Rs. {product1_price:.2f}")
print(f"{product2_name:<15}: Rs. {product2_price:.2f}")
print(f"{product3_name:<15}: Rs. {product3_price:.2f}")
print(f"Total Amount  : Rs. {total_amount:.2f}")
print(f"Discount      : Rs. {discount:.2f}")
print(f"Final Amount  : Rs. {final_amount:.2f}")

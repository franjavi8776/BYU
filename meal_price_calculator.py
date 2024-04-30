# meal price project - final submission
# this project calculates the subtotal, sales tax, total, and change based on meal prices, quantities, and sales rate

# floating point numbers
child_price_meal = float(input("What is the price of a child's meal? "))
adult_price_meal = float(input("What is the price of a adult's meal? "))
# integers numbers
children = int(input("What many children are there?  "))
adults = int(input("What many adults are there? "))

print()

subtotal = (child_price_meal * children) + (adult_price_meal * adults)
#subtotal with two decimal places
print(f"Subtotal: ${subtotal:.2f}")

print()

#discount 
discount_rate = float(input("What is the discount rate? "))
#Converts the discount rate to a percentage by dividing by 100
discount = subtotal * discount_rate / 100
#discount and subtotal with two decimal places
print(f"discount: ${discount:.2f}")
subtotal = subtotal - discount
print(f"Subtotal with discount: ${subtotal:.2f}")

print()

# tax
sales_tax_rate = float(input("What is the sales tax rate? "))
#Converts the sales tax rate to a percentage by dividing by 100
sales_tax = subtotal * sales_tax_rate / 100
#sales tax and total with two decimal places
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

print()

# payment bill
payment_amount= float(input(f"What is the payment amount? "))
change = payment_amount - total
#change with two decimal places
print(f"Change: ${change:.2f}")
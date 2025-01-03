# Vending machine menu list + base layout for the design
print("Welcome to Soda Vending Machine!!!")
print(" = Soda  Price      Code       =")
print(" | Coke |  $2  | Number : 110 |")
print(" | Dew  |  $5  | Number : 220 |")
print(" | 7Up  |  $7  | Number : 770 |")
print(" ==============================")

# Price mapping for soda items
SodaPrice = {
    110: {'name': 'Coke', 'price': 2},
    220: {'name': 'Mountain Dew', 'price': 5},
    770: {'name': '7Up', 'price': 7}
}

# Asking the customer for product code
print("Please Enter Product Code to purchase:")
customerCode = int(input())

# Check if the customer entered a valid code
if customerCode in SodaPrice:
    # Get the item name and price
    item = SodaPrice[customerCode]
    print(f"You have chosen {item['name']}.")
    print(f"== That will be ${item['price']} ==")

    # Ask for payment
    print("Insert Payment Here:")
    payment = float(input())

    # Check if payment matches the price
    if payment == item['price']:
        print(f"Thank you, you have inserted ${payment} for {item['name']}.")
    elif payment > item['price']:
        change = payment - item['price']
        print(f"Thank you, you have inserted ${payment} for {item['name']}. Your change is ${change}.")
    else:
        print("Insufficient payment. Please insert enough money.")
else:
    print("Invalid product code. Please try again.")
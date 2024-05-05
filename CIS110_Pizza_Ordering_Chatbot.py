print("Hi there! I am Soe, your virtual assistant. I can help you order a pizza!")
print("I am going to ask what you want to order. After typing an answer, press Enter.")
userName = input("\nEnter you name: ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name: ")
if userName.lower() == "soe lin":
    print(f"\nMy usual customer, {userName} has returned. Welcome back, How many more pizzas do you want to order again?")
else:
    print(f"\nHello, {userName}. Nice to meet you! It's my pleasure to assist you ordering a pizza")   
size = input("\nWhat size do you want? Enter small, medium, or large: ")
while size.lower() not in ["small", "medium", "large"]:
    size = input ("We dont have that size! Please enter small, medium, or large: ")
flavor = input("\nEnter the flavor of pizza: ")
while len(flavor) == 0:
    flavor = input ("Where is the flavor? You want a cardboard? To get to flavor town, you need to type in a valid flavor: ")
print("If you are not sure what type of crust to get, I suggest if you love a thick, doughy crust choose the Handmade Pan. For thinner crust, select the Hand Tossed pizza. For the crispiest bite, choose the Crunch thin.")
crustType = input("\nWhat type of crust do you want: ")
while len(crustType) == 0:
    crustType = input("If there is no crust, it's like eating a sandwich. Please enter a valid pizza crust: ")
quantity = input("\nHow many of these do you want to order? Enter a numberic value: ")
while not quantity.isdigit():
    quantity = input("Value is not recognzied. Please type in numeral number. 1,2,3,4,5: ")
quantity = int(quantity)
method = input("\nDo you want to do carry out or delivery?: ")
while method not in ["carry out", "delivery"]:
    method = input("How are you going to get this pizza? Please enter carry out or delivery: ")


if method.lower() == "delivery":
    deliveryFee = 5 
else:
    deliveryFee = 0 
salesTax = 1.1 
if size.lower() == "small":
    pizzaCost = 8.00
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large": 
    pizzaCost = 17.99 
    
total = (pizzaCost * quantity) * salesTax + deliveryFee 
print("-" * 10)
print(f"Thank you, {userName}, for your order.") 
print(f"Including tax, Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")

if total >= 50: 
    print("\nCongratulations! You have been awarded a $10 Off coupon for your next order.")
else:
    print("\nOrders over $50 will recive a free $10 Off Coupon for the next purchase.") 
print("-" * 10)

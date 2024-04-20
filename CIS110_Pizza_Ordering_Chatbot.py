print("Hi there! I am Soe, your virtual assistant. I can help you order a pizza!")
print("I am going to ask what you want to order. After typing an answer, press Enter.")
username = input("\nEnter you name:  ")
print(f"\nHello, {username}. Nice to meet you!")
size = input("\nWhat size do you want? Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
print("If you are not sure what type of crust to get, I suggest if you love a thick, doughy crust choose the Handmade Pan. For thinner crust, select the Hand Tossed pizza. For the crispiest bite, choose the Crunch thin Crust.")
crustType = input("\nWhat type of crust do you want:  ")
quantity = input("\nHow many of these do you want to order? Enter a numberic value:  ")
quantity = int(quantity)
method = input("\nDo you want to do carry out or delivery?:  ")

salesTax = 1.1 
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax

print("-" * 10)
print(f"Thank you, {username}, for your order.") 
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")


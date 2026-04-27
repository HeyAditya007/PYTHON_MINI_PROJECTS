# THIS IS SIMPLE SHOPPING CART PROGRAMME DON'T JUDGE ME IF I BUY LOT'S PIZZA

item = input("enter your item to buy (q to quit ):  ").upper()
total = 0 
while item != "Q":
    quantity = int(input("Enter the quantiny of your item :  "))
    price = float(input("enter the price of item:  "))
    print(f"you have bought {item} X {quantity} . ")
    item = input("enter your item to buy ( q to quit ):   ").upper()
    total += quantity * price
    print( total)





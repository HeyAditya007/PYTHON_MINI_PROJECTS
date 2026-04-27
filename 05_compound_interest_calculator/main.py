# PYTHON COMPOUND INTEREST CALCULATOR 

principle = 0 
rate = 0 
time = 0 


while principle <= 0:
    principle = float(input("enter your principle amount:   "))
    print("principle is valid now for the interest rate")
    if principle <= 0:
       print("principle can not be zero or negative")

while  rate <= 0:
    rate = float(input("enter your interest rate :  "))
    if rate <= 0:
      print("rate is not valid")


while  time <= 0:
    time = int(input("enter your time:  "))
    if time <= 0:
       print("time is not valid")

print(principle)       
print(rate)       
print(time)       
       
final_amount = principle * pow(( 1 + rate / 100 ), time)


print(final_amount)
# THIS IS SIMPLE BODY WEIGHT CONVERTER PROGRAMME IN PYTHON 
weight = float(input("enter your body weight:  "))
unit = input("enter your unit (kgs / lbs):  ")

kgs = weight / 2.2046226

lbs = weight * 2.2046226

if unit.upper() == "KGS":
    print(lbs)
elif unit.upper() == "LBS":
    print(kgs)
else :
    print("your unit is invalid.")       
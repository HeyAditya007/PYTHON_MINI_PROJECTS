# THIS IS SIMPLE PYTHON TEMPRETURE CONVERTER
temp = float(input("Enter your temperature: "))
unit = input("Enter your temperature sign (C/F): ").upper()

F = ((temp * 9) / 5) + 32
C = (temp - 32) * 5 / 9

if unit == "F":
    print(C)

elif unit == "C":
    print(F)

else:
    print("Invalid temperature sign.")
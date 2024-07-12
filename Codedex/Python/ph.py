""" Create a fuction that say when you compuest is accid or basic"""

ph = float(input("Enter the pH value: "))

if ph > 7:
    print("this compuest is basic")
elif ph == 7:  # The elif helps to make a else and if at the same time
    print("this compuest is neutral")
else:
    print("this compuest is acid")

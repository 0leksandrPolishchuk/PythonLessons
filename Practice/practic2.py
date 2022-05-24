# CURRENCY EXCHANGE CALCULATOR
print("CURRENCY EXCHANGE CALCULATOR")
print("Available Only: UAH, Euro, USD, British Pound")
currency_what = input("Enter what currency you want to exchange: ")
currency_get = input("Enter what currency you want to get: ")

print("Enter how many", currency_what, "you want exchange" + ": ", end=""),
currency1 = float(input())

print("Enter value", currency_what, "to", currency_get + ": ", end=""),
currency2 = float(input())

print("You get:", currency1 * currency2, currency_get)

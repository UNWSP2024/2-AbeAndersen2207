#UNWSP Programming PythonCos2005DEsp25
#Program_3_Total Purchase
#01.31.25
#Abraham. N. Andersen

# Prompt: A customer in a store is purchasing five items.
# Write a program that asks for each item, then displays the subtotal of the sale, the amount of sales tax,
# and the total. Assume the sales tax is 7 percent.

#Introduction
print("hello would you like to calculate, simply and easily, the total of a purchase of your's including sales tax?")

# Get the price of each item.
item1 = float(input("First enter the price of your 1st item: "))
print("")
item2 = float(input("Enter the price of the 2nd item: "))
print("")
item3 = float(input("Enter the price of the 3rd item: "))
print("")
item4 = float(input("Enter the price of the 4th item: "))
print("")
item5 = float(input("And finally enter the price of your 5th item: "))

# Calculate the subtotal.
Subtotal = item1 + item2 + item3 + item4 + item5
print(" Total price of these items is $", format(Subtotal, ".2f"))
print("")

# Calculate the sales tax.
Sales_tax = 0.07 * Subtotal
print(" Tax on these items is $", format(Sales_tax, ".2f") )
print("")

# Calculate the total.
Total = Subtotal + Sales_tax

# Display the results.
print("Given that your Subtotal is: $", format(Subtotal, ".2f"))
print("")
print("And the sales tax on all the items is: $", format(Sales_tax, ".2f"))
print("")
print("We see that your grand total is: $", format(Total, ".2f"))

#Salutation
print("")
print("")
print("Thank you for using this program. I hope it proved my abilities and had use. ;)")
print("")
print("")
print("To God be the Glory")
print('Program written by: Abraham. N. Andersen')
print('01.31.25')
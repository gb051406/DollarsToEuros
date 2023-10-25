'''
This project usees a while loop to ask to convert usd to euros until otherwise noted.
'''
# declares input for while loop
question = "yes"
#while loop
while question != "no":
    dollar = input("Enter the dollar amount to be converted: ")
    euro = float(dollar) * 0.9454
    print("Your converted amount is: " + str(euro))
    question = input("would you like to convert again? yes/no: ")
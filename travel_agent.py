'''
travelagent.py

##########################################
#### Calderdale College Travel Agency ####
##########################################

Bureau de Change system to convert from GBP 
to requested currency.

Suported currencies: GBP,USD,EUR,BRL,JPY,TRY

Version 1.02
Author: Aurora Hill
email: 257607@student.callderdale.ac.uk

'''

#set up some dictionaries to store data - leave alone
exchangeRate = {
    #"GBP":0,
    "USD": 1.40,
    "EUR": 1.14,
    "BRL": 4.77,
    "JPY": 151.05,
    "TRY": 5.68
}

#set up some variables for general use

#percentage transaction fee for up to 300GBP
baseTransactionFee = 0.035 

#percentage discount rate to apply to staff discounts 
staffDiscountRate = 0.05

#Initial status of staff member discount
staffMember = False  
transactionFee = 0

#get amount to convert
def welcome_message():  
    return("Hello\nWelcome to the Bureau De Change System")


def get_amount_to_convert():
    #ask user for ammout of GBP
    amountToConvert = input("Enter the ammount of GBP you which to convert: £")
    #Checks the entered value is a number else repetes the function
    try:
        return float(amountToConvert)
    except:
        print("You've entered a non numerical value")
        get_amount_to_convert()

#the currency the user chooses 
def get_currency_to_convert_to():
	#prints the index of currencies
    for x, y in exchangeRate.items():
        print(x,y)
		#gets currency input from user
    currencyToConvertTo = input(
        "Choose the currency to convert to from the list above: ")
    currencyToConvertTo = currencyToConvertTo.upper()

		#check to see if valid input
    for z, j in exchangeRate.items():
        if currencyToConvertTo == z:
            return currencyToConvertTo
    print("Please enter a currency form the provided list")
    get_currency_to_convert_to()

#find out if this is for a staff member
def is_staff_member():  
    staff = input("\nDo you wish for a discount to be applied Y/N: ")
    if staff.upper() == "Y":
        print("The percentage discont applied is " + str(staffDiscountRate) +
              "%")
        return True
    elif staff.upper() == "N":
        print("No discount will be applied")
        return False
    else:
        print("Please enter Y or N")
        is_staff_member()


#workout the amount after the convertion
def convert_currency(currencyToConvertTo, amountToConvert):
	multiplier = exchangeRate.get(currencyToConvertTo)
	convertedAmount = multiplier * int(amountToConvert)
	return convertedAmount


#Work out the fee
def work_out_the_fee(transactionFee, amountToConvert):
	if float(amountToConvert) > 2000:
		transactionFee += (float(amountToConvert) * 0.015)
	elif float(amountToConvert) >= 1000:
		transactionFee += (float(amountToConvert) * 0.02)
	elif float(amountToConvert) >= 750:
		transactionFee += (float(amountToConvert) * 0.025)
	elif float(amountToConvert) >= 300:
		transactionFee += (float(amountToConvert) * 0.03)
	else:
		transactionFee += (float(amountToConvert) * 0.035)
	return transactionFee


#workout the total cost
def work_out_total_cost(transactionFee,amountToConvert):
    totalCost = transactionFee + float(amountToConvert)
    return totalCost


# Leave the code below alone  **NO NEED TO EDIT IT** :)


def print_result(amountToConvert, currencyToConvertTo, convertedAmount,
                 transactionFee, totalCost, staffMember):
    print("\nThe conversion is as follows:\n")
    print("Converting %s GPB to %s results in an amount of %s %s" % (
        str(format(amountToConvert, '.2f')),
        currencyToConvertTo,
        str(format(convertedAmount, '.2f')),
        currencyToConvertTo,
    ))
    print("The transaction fee for this is %s GBP" % (str(
        format(transactionFee, '.2f')), ))

    if staffMember == True:
        discountAmount = transactionFee * staffDiscountRate
        print("A staff discount of %s GBP will also be applied" % (str(
            format(discountAmount, '.2f'))))
        totalCost = totalCost - discountAmount

    print("\nThis results in a total charge of %s GBP" % format(
        totalCost, '.2f'))

''''
print(welcome_message())
amountToConvert = get_amount_to_convert()
targetCurrency = get_currency_to_convert_to()
staffMember = is_staff_member()
convertedAmount = convert_currency(targetCurrency, amountToConvert)
transactionFee = work_out_the_fee(transactionFee,amountToConvert)
totalCost = work_out_total_cost(transactionFee, amountToConvert)
print_result(amountToConvert, targetCurrency, convertedAmount, transactionFee, totalCost, staffMember)
'''

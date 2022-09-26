'''

GUI bureau de change

GUI currency exchanger


Aurora Hill

1.0.1


'''



#imports
from guizero import App, TextBox, Text, Combo, CheckBox,Drawing
import travel_agent


#container
app = App(title="Bureo de change")
money_text = ""


#functions
def show_currency_type():
	currency_list = []
	for x, y in travel_agent.exchangeRate.items():
		currency_list.append(x) 
	return currency_list

#updater when anythig changes 
def app_update():
	money_display.clear()
	money_display.text(250-(len(input_box.value)*5), 0, "£"+input_box.value)
	output_display1.clear()
	output_display2.clear()
	cost = calculate()
	output_display1.text(60,0,text="You will recive "+str(travel_agent.convert_currency(country.value,input_box.value))+" "+str(country.value))
	output_display2.text(60,0,text="This will cost: £"+str(cost))

#cost calculater
def calculate():
	transactionFee = travel_agent.work_out_the_fee(travel_agent.transactionFee,input_box.value)
	totalCost = travel_agent.work_out_total_cost(transactionFee, input_box.value)
	if staff.value == 1:
		discountAmount = transactionFee * travel_agent.staffDiscountRate
		totalCost -= discountAmount
		return(totalCost)
	else:
		return(totalCost)

#display 
while True:
	main_text = Text(app, text = travel_agent.welcome_message())
	submain_text = Text(app, text = "\nEnter the amount you wish to convert:")
	money_display = Drawing(app, width="fill")
	output_display1 = Drawing(app, width="fill", height=30)
	output_display2 = Drawing(app, width="fill", height=30)
	input_box = TextBox(app,text="",command=app_update)
	country = Combo(app, options=show_currency_type(),command=app_update)
	staff = CheckBox(app, text="Do you want the "+str(travel_agent.staffDiscountRate*10)+"% staff discount?",command=app_update,enabled = True)
	app.display()

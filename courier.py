#Ask the user to input the price of the items they want to puchase 
#Ask the user to input the total distance of the delivery in kms 
#Set up as true some default delivery choices
#Ask the user to input their deliver preference
#If the user preference is different from the defalut choice then the value of the default choice becomes false
#Set up the conditions if the default delivery preferences turns out to be true or false 
#Add to the delivery cost accordingly 
#Print the delivery cost added to the price of the item up to 2 decimal places

price = float(input('Enter the price of the items you want to puchase: '))
distance = float(input('Enter the total distance of the delivery in kms: '))

delivery_costs = 0

air_delivery = True
full_insurance = True
gift = True
priority_delivery = True 

air_delivery_check = input('Would you like air or freight delivery? (Enter either Air of Freight) ')
if air_delivery_check == 'Freight':
    air_delivery = False 

insurance_check = input('Would you like full or limited insurance? (Enter either Full or Limited) ')
if full_insurance == 'Limited':
    full_insurance = False

gift_check = input('Is the item a gift? (Yes or No) ')
if gift_check == 'No': 
    gift = False

priority_check = input('Would you prefer priority or standard delivery? (Enter either Priority or Standard) ')
if priority_check == 'Standard': 
    priority_delivery = False 

if full_insurance == True:
    delivery_costs =+ 50 
if full_insurance == False: 
    delivery_costs =+ 25 

if gift: 
    delivery_costs += 15 
if gift == False: 
    delivery_costs += 0

if priority_delivery: 
    delivery_costs += 100 
if priority_delivery == False:
    delivery_costs += 20

if air_delivery == True:
    delivery_costs += distance*0.36
if air_delivery == False:
    delivery_costs += distance*0.25

print(round(delivery_costs + price, 2))

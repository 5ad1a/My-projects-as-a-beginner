#This programme calculate and outputs the total price of items in stock of a cafe

menu = ['item_1', 'item_2', 'item_3', 'item_4']
stock = {'item_1': 50, 'item_2': 76, 'item_3': 89, 'item_4': 24}
price = {'item_1': 1.85, 'item_2': 4.95, 'item_3': 2.25, 'item_4': 7.65}

tot_stock_value = [stock[item]*price[item] for item in menu]

tot_price = 0
for x in range(len(menu)): 
    tot_price += tot_stock_value[x] 

print(round(tot_price, 2))


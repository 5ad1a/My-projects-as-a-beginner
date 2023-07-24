product_1 = input('Enter the name of a shopping item: ')
product_2 = input('Enter the name of another shopping item: ')
product_3 = input('Enter the name of one more shopping item: ')

price_1 = float(input('Enter the price of the first item: '))
price_2 = float(input('Enter the price of the second item: '))
price_3 = float(input('Enter the price of the third item: '))

tot_price = price_1 + price_2+ price_3
average = tot_price/3
rounded_average = round(average, 2)

print('The total of ' + product_1 + ", " + product_2 + ", " + product_3 + " is " + tot_price + "and the average price of the items is £" + rounded_average)
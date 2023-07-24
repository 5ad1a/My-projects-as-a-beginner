#This function takes the number of nights the user will be staying at a hotel for
#and returns the total cost for the hotel stay

num_nights = int(input('How many nights you will be staying at the hotel for? '))

def hotel_cost(num_nights): 
    return num_nights*70 


#Thw user is asked to enter the name of the city they are flying to
#If the name of the city is not an option, the programme will ask the user to add a correct name of a city from one in the options

city = (str(input('Which city you are flying to (London, Endinburgh, Manchester, or Leicester)? '))).capitalize()
city_list = ['London', 'Endinburgh', 'Manchester', 'Leicester']
while True:
    if city not in city_list:
        city = (str(input('Please enter a valid city name from one in the options: '))).capitalize()
    if city in city_list:
        break


#This function takes the city the user is flying to as an argument and returns the cost of the flight
def plane_cost(city): 
    if city == 'London': 
        flight = 45 
    if city == 'Endinburgh': 
        flight = 120 
    if city == 'Manchester': 
        flight = 40 
    if city == 'Leicester':
        flight = 30
    return flight


#This function takes the number of days the car will be hired for 
#and returns the total cost of car rental

num_days_car_hiring = int(input('How many days you will be hiring the car for? '))

def car_rental(num_days_car_hiring):
    return num_days_car_hiring*25


#This function takes the previous three functions' arguments as arguments and return the total cost of the holiday
def holiday_cost(num_nights, city, num_days_car_hiring): 
    cost = hotel_cost(num_nights) + plane_cost(city) + car_rental(num_days_car_hiring)
    return 'The total cost for the hotel stay is £' + str(hotel_cost(num_nights)) + '.\nYour flight cost is £' + str(plane_cost(city)) + '.\nYour car rental cost is £' + str(car_rental(num_days_car_hiring)) + '.\nThe total cost for your holiday is £' + str(cost) + '.'

print(holiday_cost(num_nights, city, num_days_car_hiring))
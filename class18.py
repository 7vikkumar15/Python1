'''
from datetime import date , time , datetime
today = date.today()
now = datetime.now()

print("Today's date is " , now)
print("\n Current Date and time is " , now)

print("\n Date components" , today.year , today.month , today.day)


import random
import time

def getRandomDate (startDate , endDate):
    print("Printing random date between " , startDate , "and" , endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate , dateFormat))
    endTime = time.mktime(time.strptime(endDate , dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat , time.localtime(randomTime)) 

    return randomDate

print("Random Date = " , getRandomDate("1/1/2016","12/12/2018"))
'''

def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "Tokyo"==city:
        return 330
    elif "Kyoto" == city:
        return 220
    elif "Osawa" == city:
        return 189
    elif "Saitama" == city:
        return 198
    elif "Yokohama" == city:
        return 202
    
def rental_car_cost(days):
    if days>=7:
        return 40*days - 20
    elif days>=3:
        return 40*days-20
    else:        
        return 40*days
    

def trip_cost(city , days , spending_money):
    return rental_car_cost(days) + hotel_cost(days)+ plane_ride_cost(city)+spending_money



print("Cost of car rental: ",rental_car_cost(5))

print("Cost of plane ride: ",plane_ride_cost("Tokyo"))

print("Cost of hotel room: ", hotel_cost(7))

print("Total cost of the trip:",trip_cost("Tokyo", 3 , 3500))

print(trip_cost("Kyoto", 7 , 7500))
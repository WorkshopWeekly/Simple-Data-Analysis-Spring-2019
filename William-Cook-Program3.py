# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Weather CSV Library           |
# William S Cook                           |
# Last Modified: Feb 28, 2019              |
# -----------------------------------------+
# Peads a document and finds the values of temperature and some of the towns that are in the state being inputted |
# -----------------------------------------+
import csv
def coldest_temperature(input_file):
    file = open(input_file, "r")
    read = csv.reader(file)
    file.readline()
    cold = 1000
    for line in read:
        if int(cold) > int(line[7]):
            cold = line[7]
            state = line[5]
            day = line[4]
        else:
            cold = cold                   
    print("Coldest Fahrenheit temperature reading:", cold)
    print("Location:", state)
    print("Date:", day)
    
def average_temperature(input_file, location):
    file = open(input_file, "r")
    read = csv.reader(file)
    file.readline()
    count = 0
    average = 0
    
    for line in read:
        if line[5].lower() == location.lower(): # It reassigns the value by the inputed city or town
            count += 1
            average = int(line[0]) + average
        else:
            count += 0
    try:
        average = average/count
    except ZeroDivisionError:   # Stops the error of when the count is zero and it is trying to divid by 0
        print("Number of readings:", str(count))
        print("Average temperature: Not Applicable")
    else:
        print("Number of readings:", str(count))
        print("Average temperature:", round(average,2)) 


    
def all_stations_by_state(input_file, state):
    file = open(input_file, "r")
    read = csv.reader(file)
    file.readline()
    location = []
    
    for line in read:
        if line[11].lower() == state.lower(): #prints the towns recorded that are in the state given
            location.append(line[1])
    if len(location) == 0:
        print("There are no recording stations")
    location = set(location)
    location = list(location)
    location.sort()
    for i in range(len(location)):
        if i == 0:
            print("Recording Stations")
            print("------------------")
            print(str(i + 1) + "." + location[i])
        else:
            print(str(i + 1) + "." + location[i])


def coldest(input_file):
    file = open(input_file, 'r')
    read = csv.reader(file)
    file.readline()
    cold = 1000
    place = ""
    date = ""
    average = 0
    count = 1
    for line in read:
        if int(line[8]) > int(count):
            print("\nColdest temperature reading for month", str(count) + ": " + str(cold))
            print("Located in", str(place) + ", occured on:", str(date))
            print("Average temperature that month:", str(average))
            count += 1
            cold = 1000
        elif int(cold) > int(line[7]) and count == int(line[8]):
            cold = int(line[7])
            place = line[5]
            date = line[4]
            average = int(line[0])
            month = int(line[8])  
        else:
            continue
    print("\nColdest temperature reading for month", str(count) + ": " + str(cold)) # Wouldn't work for last month
    print("Located in", str(place) + ", occured on:", str(date))  # placing the print statement here allows us to print the final values
    print("Average temperature that month:", str(average))  # with a month value larger than the count
    
    
# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+

def menu():
    print()
    print("1. Identify coldest temperature.")
    print("2. Identify average temperature for a given location.")
    print("3. Identify all recording station locations by state.")
    print("4. Identify information about the loaction with the coldest temperature for each month")
    print("5. Quit.")
    print()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "weather.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            coldest_temperature(input_file)
        elif (choice == 2):
            location = input("Enter desired location (e.g. Miles City, MT): ")
            average_temperature(input_file, location)
        elif (choice == 3):
            state = input("Enter name of state (e.g. Montana): ")
            all_stations_by_state(input_file, state)
        elif (choice == 4):
            coldest(input_file)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()

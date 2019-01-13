cars = 100 # This sets the variable cars to a value, 100
space_in_a_car = 4 # This sets the variable space_in_a_car to a value, 4
drivers = 30 # This sets the variable drivers to a value, 30
passengers = 90 # This sets the variable passengers to a value, 90
cars_not_driven = cars - drivers # This sets the variable cars_not_driven to the value resulting from subtracting the number of drivers from the number of cars
cars_driven = drivers # This sets the variable cars_driven to the number of drivers
carpool_capacity = cars_driven * space_in_a_car # This sets the variable carpool_capacity to the value resulting from multiplying cars_driven by space_in_a_car
average_passengers_per_car = passengers / cars_driven # This sets the variable average_passengers_per_car to the variable resulting from dividing the number of passengers by the number of cars_driven


# This will print the statement, "There are 100 cars available."
print "There are", cars, "cars available."

# This will print the statement, "There are only 30 drivers available."
print "There are only", drivers, "drivers available."

# This will print the statement, "There will be 70 empty cars today."
print "There will be", cars_not_driven, "empty cars today."

# This will print the statement, "We can transport 120.0 people today."
print "We can transport", carpool_capacity, "people today."

# This will print the statement, "We have 90 to carpool today."
print "We have", passengers, "to carpool today."

# This will print the statement, "We need to put about 3 in each car."
print "We need to put about", average_passengers_per_car, "in each car."


# From "Exercise 4: Variables and Names" by Learn Python the Hard Way.
# I learned how to set variables with particular values, how to set variables that perform a computation based on those values (i.e., based on other variables), and how to print statements that include variables in the outputs.
# I practiced using python as a calculator again, e.g., python -c "print 100 - 30". This time, I hit a wall: I couldn't figure out how to assign variables within Terminal and then print them using python -c. For example, if in terminal I set x=5 and y=10, and then I tried to run python -c "print x + y", it would not work. The reason, I discovered, was a misunderstanding on my part. To use "python as a calculator", you simply need to run python in Terminal, and within that, you can set variables and print statements as above. Cool stuff.

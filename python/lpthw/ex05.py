name = 'Zed' # This sets the variable name to Zed
age = 35 # This sets the variable age to a value, 35
height = 74 # inches; this sets the variable height to a value, 74
height_cm = height * 2.54 # centimeters; this sets the variable height_cm to the value resulting from converting the height from inches to centimeters, using the standard formula for that conversion
weight = 180 # lbs; this sets the variable weight to a value, 180
weight_kg = weight / 2.205 # kilograms; this sets the variable weight_kg to the value resulting from converting the weight from pounds to kilograms, using the standard formula for that conversion
eyes = 'blue' # This sets the variable eyes to Blue
teeth = 'white' # This sets the variable teeth to White
hair = 'brown' # This sets the variable hair to Brown

# This will print the format string into the statement, "Let's talk about Zed."
print "Let's talk about %s." % name

# This will print the format string into the statement, "He's 74 inces tall, which is 187 cm"
print "He's %d inches tall, which is %d cm." % (height, height_cm)

# This will print the format string into the statement, "He's 180 pounds heavy."
print "He's %d pounds heavy." % weight

# This will print the string into the statement, "Actually, that's not heavy."
print "Actually that's not heavy."

# This will print the format string into the statement, "(Especially if you convert that into kilograms: 81 kg. See?)"
print "(Especially if you convert that into kilograms: %d kg. See?)" % weight_kg

# This will print the format string into the statement, "He's got blue eyes and brown hair."
print "He's got %s eyes and %s hair." % (eyes, hair)

# This will print the format string into the statement, "His teeth are usually white depending on the coffee."
print "His teeth are usually %s depending on the coffee." % teeth

# This will print the format string into the statement, "If I add 35, 74, and 180 I get 289."
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# From "Exercise 5: More Variables and Printing" by Learn Python the Hard Way.
# I learned about strings, in particular format strings, which let you print statements that include variables within them.
# I observed that %s is the formatter used for text and %d is the formatter used for numbers.

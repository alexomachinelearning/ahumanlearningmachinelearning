# This sets the variable `x` as a format string that outputs the following: "There are 10 types of people." The formatter %d tells python to insert the value 10 at the location of %d
x = "There are %d types of people." % 10

# This sets the variable `binary` as the string, "binary"
binary = "binary"

# This sets the variable `do_not` as the string, "don't"
do_not = "don't"

# This sets the variable `y` as a format string that outputs the following: "Those who know binary and those who don't." The formatters %s and %s tell python to insert the variables `binary` and `do_not`, in the order specified in parentheses
y = "Those who know %s and those who %s." % (binary, do_not)

# This command tells python to print the output of the variable `x`
print x

# This command tells python to print the output of the variable `y`
print y

# This command tells python to print a string with the output, "I said: 'There are 10 types of people.'"
print "I said: %r." % x

# This command tells python to print a string with the output, "I also said: 'Those who know binary and those who don't.'."
print "I also said: '%s'." % y

# This sets the variable `hilarious` to the evaluation, False

hilarious = False

# This sets the variable `joke_evaluation` as a format string that outputs the following: "Isn't that joke so funny?! False"
joke_evaluation = "Isn't that joke so funny?! %r"

# This command tells python to print the output of the variable `joke_evaluation` along with the output of the variable `hilarious`: "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

# This sets the variable `w` as the string, "This is the left side of..."
w = "This is the left side of..."

# This sets the variable `e` as the string, "a string with the right side."
e = "a string with a right side."

# This command tells python to print the output of the variable `w` along with the output of the variable `e`: "This is the left side of...a string with a right side."
print w + e

# End of original assingment
# Below, I practice some of what I've learned by creating a fictitious back-and-forth with my computer.

print "..."
print "That concludes this LPTHW exercise."
print "[Initiate Self-Assessment Program]"
print "That was nice, but I think I'll give myself an assignment now."
print "Computer, let's print my name."
print "Set variable my_name equal to 'Alex'."

my_name = "Alex"

print "Computer: Confirmed."
print "Set variable my_middle_initial equal to 'O'."

my_middle_initial = "O"

print "Computer: Confirmed."
print "Set variable my_last_name equal to 'Machine Learning'."

my_last_name = "Machine Learning"

print "Computer: Confirmed."
print "Set variable ask_question equal to 'What is my name?'"

ask_question = "What is my name? "

print "Computer: Confirmed."
print "Set variable give_response equal to ''%s %s %s' % (my_name, my_middle_initial, my_last_name)'"

give_response = "%s %s %s" % (my_name, my_middle_initial, my_last_name)

print "Computer: Confirmed."

print "Now print 'ask_question + give_response'"

print "Computer: Confirmed."
print "Computer: Now printing..."
print ask_question + give_response

print "Hooray! That worked! Great work, Computer!"
print "..."
print "Computer: You could probably simplify this by using a full_name variable."
print "Good observation, computer...hey, how did you get so smart!?"
print "[That concludes this adventure]"


# From "Exercise 6: Strings and Text" by Learn Python the Hard Way
# I learned about a new format string, %r, useful for debugging, and I learned that you can insert strings inside others (i.e., set a variable to output a string that contains another string)
# I decided to give myself a short self-assessment to practice the use of strings. It took a long time to think through, but it was fun! I imagine there's a simpler way to write the code, but I'm not there quite yet.

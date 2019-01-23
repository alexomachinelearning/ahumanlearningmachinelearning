# There appear to be multiple ways to print the same content in python

# This command tells python to print, "Alex went to Starbucks". Note that the argument is set directly with the print command
print "Alex went to Starbucks"

# The following three arguments tell python to set the variable `name` to "Alex", the variable `action` to "went to", and the variable `place` to "Starbucks"
name = "Alex"
action = "went to"
place = "Starbucks"

# This command also tells python to print, "Alex went to Starbucks". Note that the variables were already set above
print name, action, place

# This command also tells python to print, "Alex went to Starbucks". Note that in this option, the formatter `%s` in the format string is used to tell python how many arguments to print, and the variables in parentheses tell python which strings to present
print "%s %s %s" % (name, action, place)

# This command also tells python to print, "Alex went to Starbucks". Note that in this option, spaces are manually interspersed between the three variables
print name + " " + action + " " + place

# This command tells python to print, "Alex went to Starbucks to buy a cup of coffee". Note that in this option, a string is added to the argument without needing a `%s` formatter
print name + " " + action + " " + place + " to buy a cup of coffee"

# This command also tells python to print, "Alex went to Starbucks to buy a cup of coffee". Note that in this option, a `%s` formatter is used to append the last string
print name, action, place, "%s" % ("to buy a cup of coffee")

# The next two arguments tell python to set the variable `coffee_days` to "Mondays Tuesdays Wednesdays Thursdays Fridays" and to set the variable `sunniest_months` to "Juny, July, August, and September"
coffee_days = "Mondays Tuesdays Wednesdays Thursdays Fridays"
sunniest_months = "June, July, August, and September"

# This command tells python to print nothing but an empty space, to create a break for the next portion of my exercise
print ""

# This command tells python to print, "Mondays Tuesdays Wednesdays Thursdays Fridays <~ these are the days when I drink teh most coffee"
print coffee_days, "<~ these are the days when I drink the most coffee"

# This command tells python to print, "During Seattle's sunniest months of June, July, August, and September, I tend to spend less time drinking coffee and more time with ice cream in hand."
print "During Seattle's sunniest months of" + " " + sunniest_months + ", I tend to spend less time drinking coffee and more time with ice cream in hand."

# This command tells python to print "[And now for a short poem]". Note that the first set of triple-quotes creates a space above the printed text
print """
[And now for a short poem]"""

# This command tells python to print "Summertime dances: No rain to distract the clouds. We shimmer and smile." in the structure of a haiku
print """
Summertime dances:
No rain to distract the clouds.
We shimmer and smile."""

# The End

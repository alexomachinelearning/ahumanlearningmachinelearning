# This command tells python to print the output "Mary had a little lamb."
print "Mary had a little lamb."

# This command tells python to print a string with the output "Its fleece was white as snow." Note that the string, "snow", is not a variable
print "Its fleece was white as %s." % 'snow'

# This command tells python to print the string "And everywhere that Mary went."
print "And everywhere that Mary went."

# This command tells python to print the string "..........". Note that the command includes an operation that multiplies the text string, "." by 10
print "." * 10

end1 = "C" # This sets the variable `end`1 as the string "C"
end2 = "h" # This sets the variable `end2` as the string "h"
end3 = "e" # This sets the variable `end3` as the string "e"
end4 = "e" # This sets the varibale `end4` as the string "e"
end5 = "s" # This sets the variable `end5` as the string "s"
end6 = "e" # This sets the variable `end6` as the string "e"
end7 = "B" # This sets the variable `end7` as the string "B"
end8 = "u" # This sets the variable `end8` as the string "u"
end9 = "r" # This sets the variable `end9` as the string "r"
end10 = "g" # This sets the variable `end10` as the string "g"
end11 = "e" # This sets the variable `end11` as the string "e"
end12 = "r" # This sets the variable `end12` as the string "r"

# This command tells python to print the string "Cheese". Note that the command concatenates the strings `end1` through `end6` in the output string. Also note that by adding a comma after the variable `end6`, python appends the very next print commany to the same line. Without a comma immediately after `end6`, python prints the two commands on separate lines
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# [This concludes the LPTHW exercise]
# Below I play around with a few python commands that output the same statement, "Mary had a little lamb. Her fleece was white as snow. And everywhere that Mary went."
print "This concludes this LPTHW exercise."
print "[Initiate Self-Assessment Program]"
print "%s %s %s" % ("Mary had a little lamb.", "Her fleece was white as snow.", "And everywhere that Mary went.")
print "%s. %s. %s" % ("Mary had a little lamb", "Her fleece was white as snow", "And everywhere that Mary went")
name = "Mary"
print "%s %s. %s. %s %s %s." % (name, "had a little lamb", "Her fleece was white as snow", "And everywere that", name, "went")
had = "had a little lamb."
fleece = "Her fleece was white as snow."
went = "And everywhere that %s went." % name
print name, had, fleece, went
food = end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12 + "."
print name, "had a little", food, "Her fleece was full of ketchup.", went
print "Computer:", "." * 3
print "Computer: Okay, I think that's enough for you, Alex."
print "[The End]"

# From "Exercise 7: More Printing" by Learn Python the Hard Way
# I learned that you can embed one string inside another even if the embedded string is not a variable, for example, 'snow' in line 5. I also learned that you can command python to print multiple variables in a single output (concatenated) and that, by adding a comma after the last variable in a print command, python will print the next print command on the same line as the command with the comma
# I observed that

# This sets the variable `formatter` to the format string "%r %r %r %r"
formatter = "%r %r %r %r"

# This command tells python to print the output "1 2 3 4"
print formatter % (1, 2, 3, 4)

# This command tells python to print the output "'one', 'two', 'three', 'four'"
print formatter % ("one", "two", "three", "four")

# This command tells python to print the output "True False False True"
print formatter % (True, False, False, True)

# This command tells python to print the output "'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'". Note that this inserts the original variable into the output a total of four times, on purpose, which outputs a total of 16 formatters in the output string
print formatter % (formatter, formatter, formatter, formatter)

# This command tells python to print the output "'I had this thing.' 'That you could type up right.' 'But it didn't sing.' 'So I said goodnight.'". Note that using a comma after the first three strings is necessary to satisfy the number of arguments python expects, which in this instance is four, as specified in the variable `formatter`
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# From "Exercise 8: Printing, Printing" from Learn Python the Hard Way
# I learned that when printing a string with a variable that includes more than one argument, you need to use commas between the arguments in order for that command to execute correctly.
# I observed that I still don't quite understand when to use the formatter ``%s` and when to use ``%r`. However, when I temporarily changed the formatters in the variable `formatter` from "%r" (as per the original instructions in the exercise) to "%s", the output in my Terminal was visually cleaner, i.e., the 2nd, 4th, and 5th commands printed without any quotes :). Alas, it's a mystery to me why python chose to print line 20 with double-quotes yet lines 18, 19, and 21 with single-quotes.

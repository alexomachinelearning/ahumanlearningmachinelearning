# + this operator performs addition
# - this operator performs substraction
# / this operator performs division
# * this operator performs multiplication
# % this operator performs a modulo operation
# < this operator performs a comparison to see if the value on the left evaluates to less than the value on the right
# > this operator performs a comparison to see if the value on the left evaluates to greater than the value on the right
# <= this operator performs a comparison to see if the value on the left evaluates to less than or equal to the value on the right
# >= this operator performs a comparison to see if the value on the left evaluates to greater than or equal to the value on the right

# This will print the statement, "I will now count my chickens:"
print "I will now count my chickens:"

# This will print the number of hens (30) and roosters (97)
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

# This will print the statement, "Now I will count the eggs:"
print "Now I will count the eggs:"

# This will print the the number of eggs (6.75 if using floating point numbers, or 7 otherwise)
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# This will print the statement, "Is it true that 3 + 2 < 5 - 7?"
print "Is it true that 3 + 2 < 5 - 7?"

# This will print the word, "False, because the result on the left is not in fact less than the result on the right"
print 3 + 2 < 5 - 7

# This will print each of the statements / questions below, as well as each of their responses (5 and -2, respectively)
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

# This will print the statement, "Oh, that's why it's False."
print "Oh, that's why it's False."

# This will print the statement, "How about some more."
print "How about some more."

# This will print the following three statements / questions, as well as each of their responses (True, True, and False, respectively)
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

# This is Exercise 3: Numbers and Math from "Learn Python the Hard Way".
# I learned that the modulus follows the same order of operations as does multiplication or division; how to use help() when invoking python in Terminal; that running python -c from Terminal enables in-line use of python as a calculator; and how to combine text and a mathematical calculation in a single print statement.
# I noticed that when printing text, you use "", but when printing numbers, you simply type the numbers and operators without "". I also observed that Python 2 follows the convention of print "message" whereas Python 3 uses print("message") instead. I'm using Python 2 for these exercises.

# The code in this file is used in the article, "My Python Joy: A Beginner's Journey up the Programming Mountain" at https://www.linkedin.com/pulse/my-python-joy-beginners-journey-up-programming-mountain-alex-ortiz/. The purpose of that article is to introduce the LinkedIn Series "My Python Joy" to readers. This code is used in various portions of the article for stylistic or illustrative reasons

# ==========
# Introduction
# ==========

print "Why This Topic, Why Python?"

# ==========
# Why This Topic, Why Python?
# ==========

print "%s %s" % ("What's a", "Linkedin Series?")

# ==========
# What's a LinkedIn Series?
# ==========

pronoun1 = "Who "
verb = "Am "
pronoun2 = "I"
punctuation = "?"

print pronoun1 + verb + pronoun2 + punctuation

# ==========
# Who Am I?
# ==========

who = "You"

print "What %s Can Expect in This Series" % who

# ==========
# What You Can Expect in This Series
# ==========

print """The Coffee Rule

When interacting with fellow subscribers,

1. Disagree with ideas, not persons
2. Operate with empathy
3. Prioritize courtesy
"""

print "Now time for the fun stuff!"
print "3..."
print "%s" % ("2...")

final_countdown = "1..."


print final_countdown

who = "I"
action = "introduce"

print who + " " + action + " " + "%s %s" % ("to", "you") + "..."

print """My
Python
Joy
:)
"""

# ==========
# My Python Joy: A Beginner's Journey up the Programming Mountain
# II. Cool Stuff I've Learned So Far
# A: Multiple Ways to Print the Same Thing
# ==========

# I
print "My Python Joy is fun"

# II
series = "My Python Joy"
verb = "is"
adjective = "fun"

print series, verb, adjective

# III
series = "My Python Joy"
verb = "is"

print series, verb, "fun"

# IV
print "%s %s %s %s %s" % ("My", "Python", "Joy", "is", "fun")

# V
series = "My Python Joy"

print series, "%s %s" % ("is", "fun")

# Additional
series = "My Python Joy"

print series, "%s %s" % ("is", "fun") + ", says Alex..." + "but I'll be the judge of that!"

# ==========
# My Python Joy: A Beginner's Journey up the Programming Mountain
# II. Cool Stuff I've Learned So Far
# B: Python as a Super-fast Calculator
# ==========

print 2**56

print 2**128

print 2**256

print float(2**56)
print float(2**128)
print float(2**256)

print "{:,}".format(2**56)

print "{:,}".format(2**128)

print "{:,}".format(2**256)

# ==========
# In Conclusion
# ==========

print "On the command line, there's room for everybody."

# Till next time :)

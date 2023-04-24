import time
from happy import Happy

# Create a happy smiley, which is a subclass of Smiley
smiley = Happy()

# This is a form of #polymorphis, as the Happy smiley class
# does not have a method called .show(). This means that
# the method .show() of the base class {Smiley} will be
# used in stead. There is no need to specify the base
# class, like in other, statically typed, languages.
smiley.show()

# Just a short delay
time.sleep(1)

# Another form of polymorphism:
# The method blink is implemented by the Happy class, but
# is defined as an interface (i.e., an abtract base class
# with an abstract method).
smiley.blink()

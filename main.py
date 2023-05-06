""""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""
import time

from happy import Happy
from sad import Sad

if __name__ == '__main__':
    # This is only needed if you have not deleted sense_hat.py
    # and only in some environments - uncomment only if you have errors
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################

    # Create a happy smiley, which is a subclass of Smiley
    smiley = Happy()

    # This is a form of #polymorphism, as the Happy smiley class
    # does not have a method called .show(). This means that
    # the method .show() of the base class {Smiley} will be
    # used in stead. There is no need to specify the base
    # class, like in other, statically typed, languages.
    smiley.change_complexation(smiley.YELLOW, smiley.BLANK)    
    smiley.show()

    # Just a short delay
    time.sleep(1)

    # Another form of polymorphism:
    # The method blink is implemented by the Happy class, but
    # is defined as an interface (i.e., an abstract base class
    # with an abstract method).
    smiley.blink()

    sad = Sad()
    sad.change_complexation(smiley.BLUE, smiley.BLANK)
    sad.show()
    time.sleep(1)
    sad.blink()




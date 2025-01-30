from happy import Happy
from sad import Sad
from angry import Angry

def main():
    # Create an instance of Happy smiley
    happy_smiley = Happy()  # This will use the default yellow complexion
    happy_smiley.show()  # Display the smiley on the SenseHat (mock or real)

    # You can add other instances here to test other smiley expressions
    sad_smiley = Sad()  # This will be blue
    sad_smiley.show()

    angry_smiley = Angry()  # This will be red
    angry_smiley.show()

if __name__ == "__main__":
    main()

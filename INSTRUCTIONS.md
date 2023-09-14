# Accessible Version: RIOT-AT2-Part2

## Scenario / Background

In this Portfolio Task, we're going to focus on the four pillars of Object-Oriented Programming (OO):

1. Abstraction
2. Polymorphism
3. Inheritance
4. Encapsulation

### Download Project Files

Download the project files (including this `INSTRUCTIONS.md`) from [GitHub Repository](https://github.com/NM-TAFE/civ-ipriot-smiley/tree/udl/accessible).

To clone the repository, use the following command:

```bash
git clone https://github.com/NM-TAFE/civ-ipriot-smiley.git
```

The project contains various classes. Some are "base classes" (also known as super classes), and some are "subclasses," derived from the base classes.

---

## Questions and Tasks

### Understanding the Classes

Answer the following questions:

a. How many classes can you identify in the project?
b. In your own words, describe how 'abstraction' is implemented in this project.
c. List the classes that are subclasses and the ones that are base (or super) classes.
d. What is the name of the process of deriving from base classes?

### Not All Classes Are the Same

Investigate the `Happy` and `Sad` classes. 

Answer the following:

- Commonalities between `Happy` and `Sad`
- Differences between `Happy` and `Sad`
- Note any feature that stands out as a significant difference.

### Where's the Sense(Hat) in That?

Answer the following questions:

a. In which class is SenseHat used?
b. What functionalities of SenseHat are utilized?
c. What is the term for storing and potentially hiding objects within classes?

### Sad Smileys Can't Blink (Or Can They?)

Perform the following tasks and answer any associated questions:

a. Describe how the `blink()` method in the `Happy` class makes the smiley blink.
b. Create a new method called `blink` in the `Sad` class:

   ```python
   def blink(self, delay=0.25):
       pass  # your implementation goes here
   ```
c. Implement the code for the `blink` method. Take guidance from the `Happy` class. Focus on outputting a print statement to signify a "blink," and use the delay for the speed.
d. Test the code on your Raspberry Pi or with the provided classes. Ensure the sad smiley blinks accordingly.

> Note: Double-check wording for accessibility for people with visual impairment.

### If It Walks Like a Duck…

Answer the following:

a. What type of class is `Blinkable`? (Hint: Check its super class.)
b. What is another name for a class like `Blinkable`, which may be implemented by other classes?
c. Which OO principle does the answer from the previous question exemplify? Choose from: Abstraction, Polymorphism, Inheritance, and Encapsulation.
d. Explain how you could implement blinking in `Sad` without using `Blinkable`.
e. What is this capability called in Python, and why doesn't it work in some languages like C#?

### Does a Smiley Have to Be Happy?

Answer the following:

a. What emotions are defined in the project and where are they located?
b. Where are emotions and emoticons used in the project?
c. Suggest an easy, albeit naive, way to change the emotion of a smiley (e.g., making it "sad").

---

Go ahead and change the implementation as per the instructions above.

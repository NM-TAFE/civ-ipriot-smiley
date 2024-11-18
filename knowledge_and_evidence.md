<style>

body {
    counter-reset: h2counter;
}

/* H1 - No numbering */
h1 {
    /* No counter reset or increment */
}

/* H2 - Level 1 numbering */
h2 {
    counter-reset: h3counter;
}

h2::before {
    counter-increment: h2counter;
    content: counter(h2counter) ". ";
}

/* H3 - Level 2 numbering */
h3 {
    counter-reset: h4counter;
}

h3::before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) " ";
}

/* H4 - Level 3 numbering (optional) */
h4 {
    counter-reset: h5counter;
}

h4::before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) " ";
}

</style>

# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## Required evidence

### Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file
* Output of main.py evidence:
![main.py_output](.\docs\images\Q2.1_main.py_output.png)

* Project directory evidence:
![project_directory](.\docs\images\Q2.1_project_directory.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name   | value                   |
   | ----------              |--------|-------------------------|
   | built-in primitive type | dimmed | True (Boolean)          |
   | built-in composite type | WHITE  | (255, 255, 255) (Tuple) |
   | user-defined type       | Smiley | class                   |    
    

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type                                                         |
   | ------------             |--------------------------------------------------------------|
   | self.pixels              | a list of tuples                                             |
   | A member of self.pixels  | a tuple                                                      |
   | self                     | instance of the class used to access attributes of the class |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File     | First line                          | Line range |
   | ------------ |----------|-------------------------------------|------------|
   |  sequence    | happy.py | 39  self.draw_eyes(wide_open=False) | to line 43 |
   |  selection   | sad.py   | 27  if wide_open:              | to line 29 |
   |  iteration   | happy.py | 21  for pixel in mouth:                                | to line 22 |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used? | Example                                              |
   | ----------------------- |-------|------------------------------------------------------|
   | int                     | yes   | pixel e.g. pixel in mouth                            |
   | float                   | yes   | delay=0.25                                           |
   | str                     | no    | NA but example of my own would be message = "Hello!" |
   | bool                    | Yes   | dimmed=True , wide_open=True                         |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> * class variable example: WHITE
>
> This class variable is shared across all instances of the class Smiley and can be accessed from the class and instance of the class. 
> 
>* instance variable example: self.pixels
>
> This instance variable is unique to the instance of the class Smiley and can be accessed from the instance of the class but not a class attribute. 

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

   > The constructor in general is `__init__()` method. This method is called when a new instance of the Happy class is created. 
   > 
   > In Happy the constructor is followed by `super().__init__()`. `super()` calls the method of the superclass. The superclass of Happy is Smiley then Blinkable. Happy inherits from these two classes and will initisialise the code from the super class prior to the subclass Happy. 
   >

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   > First of all it will excute the `__init__()` method from Smiley. This method is the initialisation for the frame of the face/ blank face with the 8x8 blank and yellow pixel display. 
   > Statements:
   > * self.sense_hat = SenseHat() creates an instance of SenseHat and assigns it to the instance variable self.sense_hat
   > * line 15 and 16 assigns Y and 0 to self.(a colour for the pixels, yellow or blank)
   > * line 18-25 is the 8x8 pixel display. 
   > 
   > 
   >  Then moves to the Blinkable class, but there is no `__init__()` method so it does not initialise anything in Blinkable. 
   > 
   > Finally, happy `__init__()` is executed on lines 13 and 14.
   > Statements: 
   > * self.draw_mouth() This calls the draw_mouth method to blank out the mouth. 
   > * self.draw_eyes() This calls the draw_eyes method to blank out the eye positions. 
   >  



### Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:
   
> The code is written in PEP 8 style. 
> SenseHat is written in PEP8. This is evident when SenseHat is use in Smiley. It uses camel case as well as underscores to seperate words in variable names e.g.  self.sense_hat.low_light
> The reason the code is the same style is because the Smiley class calls for SenseHat which is a composition of Smiley. SenseHat is a module that is imported by Smiley. Maintaining consistent coding style across the linked codes helps ease of understanding the code, integration of the classes easier, uniformity for the developers to avoid confusion are just a few reasons. Also, the SenseHat is the code for the real hardware for the real LED light display whereas the other code we are using is for a simulated version. Having the same style code makes it easier to switch between the real and the simulated version.   

2. List three aspects of this convention you see applied in the code.

> * CamelCase lettering for the class names e.g. SenseHat 
> * Method names lower case and seperated by underscores e.g. draw_mouth
> * 4 space indentation style.  
>

3. Give two examples of organizational documentation in the code.

> * Docstrings are used to explain what the functionality of the code is or give a specific instruction. e.g. in Happy.py line 8 states the functionality of the Happy class is "Provides a Smiley with a happy expression". There are also docstrings under the methods to explain the purpose of the method. e.g. in Happy, under the draw_mouth method, line 18 "Renders a mouth by blanking the pixels that form that object."
> * Comments are used to give clarity on the line of code. e.g. in Smiley, line 12 "# We have encapsulated the SenseHat object". This lets the developer know the SenseHat instance has been created within Smiley but the code of SenseHat is hidden from the outside world. 
>

### Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s) |
|------------|---------------|------------------|
|  
| Happy      | Sub           | Smiley           |
| Smiley     | Super         | SenseHat         |    
| Sad        | Sub           | Smiley           |    
| Blinkable  | Super         | ABC              |    


2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Abstraction is a way to simplify the code on the surface. Exposing what the class does but not how it is done. The how it is done is defined in the sub classes that are Blinkable. 
>
> In the Blinkable class, the blink method is defined and is an abstract method. This means that the subclasses that use Blinkable have the ability to blink. But the subclasses will define the behaviour of the blink.   
> 
> There is a blink method that is defined in happy and in main when an instance of Happy is created called smiley and blink is called this calls for the blink action created in Happy. 

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> The process of deriving from a super class to a sub class is inheritance. The main purpose of inheritance in this project is to reuse code from other classes. For example, Smiley is a super class and happy is a subclass. In question 2.2.6.ii I mentioned that the Happy initialisation method calls the initialisation method from Smiley. This is where Happy inherits the frame of the face/blank face from Smiley and the dim_display and show method. This is so the code does not have to be re-written in Happy and Sad.   
>

### Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > * The pixels for the mouth are different in the draw_mouth method. The Sad class defines the pixels that draw a sad mouth and the Happy class defines the pixels that draw a smiley mouth. 
   > 
   > * Also the Blinkable behaviour is not present in the Sad class. There is no method for blink also Sad does not inherit from Blinkable like Happy does. 
   >


2. What are the key similarities?
   > * Both Happy and Sad inherit from Smiley. 
   > * Both have BLANK eyes wide_open and YELLOW eyes when closed. 
   >
3. What difference stands out the most to you and why?
   > 
   > Happy inherits from Blinkable as well as Smiley > `class Happy(Smiley, Blinkable):` However Sad does not inherit from Blinkable. Sad does not have the Blinkable functionality or a defined blink method. 
   >
4. How does this difference affect the functionality of these classes
   > There is no blink method in Sad so it cannot blink. Whether it inherits from Blinkable or not does not matter. But inheriting from Blinkable ensures that Sad needs to have a blink method. Happy inherits from Blinkable giving it the ability to blink. Happy also defines a blink method to give it the instructions of how to blink and how long for.  
   >

### Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   > Smiley because the instance ` self.sense_hat = SenseHat()` of SenseHat is in the Smiley class and is assigned to the `self.sense_hat` attribute and methods are defined to control the SenseHat. 
   > 
   > As both Happy and Sad inherit from Smiley, they inturn utilise the functionality from SenseHat because they have access to the methods of `dim_display` and `show`. These are the methods that interact with the SenseHat. 
   >  
2. Which of the SenseHat's functionalities does it utilise?
   > The functionalities of the SenseHat that are utilised is the intensity of the display (low or high) and showing the smiley on the screen by illuminating the pixels with a specific colour defined in self.pixels. Happy and Sad modify the pixels illuminated to draw a happy/sad mouth or blink (in Happy).    

3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > SenseHat is encapsulated within an instance `self.sense_hat = SenseHat()` in the Smiley class. This means that the SenseHat class cannot be accessed outside the Smiley class, it is protected from the outside. The two methods defined in Smiley allow for interaction with the SenseHat hardware through the instance of a SenseHat. Encapsulating the SenseHat within Smiley allows for a simplified code to interact with SenseHat. 
   >

### Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> No. Only Happy can blink. Sad cannot blink because it does not inherit from Blinkable, nor does it have a defined blink method. There is no blink method in the super class 'Smiley' therefore it is not inherited into Happy or Sad when the `super().__init__()` is called. 
>

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> No. The blink method is defined in the subclass, therefore if Sad was to inherit from Blinkable, the blink method would still need to be defined in the Sad class and this can be different to how Happy blinks. Inheriting from Blinkable just ensures that the subclass is blinkable.  
>

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Polymorphism refers to many forms and in the context of 'blink' this means that the blink method inherited from Blinkable can take on many forms and therefore can be defined in each subclass to be different from the other. So the 'blink' method name in each subclass is related by the common superclass 'Blinkable'.  
> For example, in Happy the delay of the blink close to blink open is 0.25 seconds. If a blink method was to be defined in Sad, this delay could be modified to keep the eyes closed longer to make the Smiley look sad. 

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> Inheritance is used in the blink method because the subclasses inherit the method called 'blink' defined in the Blinkable class. In the subclass, the blink method is then morphed to be specific to that type of Smiley.  
>
1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
   def blink(self, delay=0.25):
       pass  # Replace 'pass' with your implementation
   ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

    ```python 
     def blink(self, delay=0.25):
        """
       Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
    ```

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

![Sad Smiley Blinking](.\docs\images\CC_sad_smiley_screenshot.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > When it blinks it looks like it has no eyes as they are completely yellowed out. Could either change eye colour or only half close the blinking eye? 

  ### If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

     > Blinkable is a superclass.

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.

  > Abstract class. 

  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

  > Abstraction. This is because Blinkable defines an abstract method called `blink` but does not specify it's functionality. 
  > When the abstract method `blink` is inherited by the subclass e.g. `happy`, the subclass can define the method `blink` and the specifics. 

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

  > It is possible to grant the Sad Smiley a blinking feature without importing blinkable from Blinkable class. This is done simply by defining a method in Sad called `blink()`. Python allows the method to be reused in Sad and this is because Python is a dynamically typed language. 

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

  > This concept is called `Duck Typing`. In Python and dynamically typed languages it means that the type of an object can be defined by the methods and attributes within the class. E.g. the Sad class has the same `blink()` method as Happy but they are not linked by inheritance of Blinkable because Sad does not inherit from Blinkable like Happy does. 
  > However, this would not be possible in statically typed languages because the method will not be recognised if it is not declared from an interface or inheritance.

  ***

  ## Refactoring

  ### Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > The colours white, green, red, yellow and blank. They are defined in Smiley class.
 
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > The variable type defining the colour in Smiley is a tuple. They are not going to change because they are a 'constant' defined by the variable name being written in uppercase.
        They are also a class attribute and they are inherited by the Sad and Happy class that inherit from Smiley. 
     3. Add the color blue to the appropriate class using the appropriate format and values.

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > In the `__init__` method of Smiley the defined colours yellow and blank are used to create the face shape/pixels. In the subclasses, Happy and Sad, the mouth area uses defined colours from Smiley to create the mouth and eyes by using blank colour/ pixels. 

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > Easiest way would be to change the default colour in the superclass. E.g.`Y = self.YELLOW` change to replace YELLOW with GREEN `Y = self.GREEN`. This will change all the smileys to green.  

  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

![Smiley Add Complexion](.\docs\images\CC_smiley_complexion.png)


  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

![Sad Refactor](.\docs\images\CC_sad_git_refactor.png)

![Happy Refactor](.\docs\images\CC_happy_git_refactor.png)

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.
        > Abstraction. Because the details of the complexion (colour) is stored in the super class. The subclass just calls for the complexion method. The colour management is done by Smiley for the face.
        >               

  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.

![Comlexion Remains Yellow](.\docs\images\CC_complexion_yellow.png)

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

![Add Complexion to __init__](.\docs\images\CC_complexion_default_yellow.png)
  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.
![My Complexion Variable](.\docs\images\CC_my_complexion.png)
  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

> I had already manually changed all the Y's to C's previously. So I will now refactor from C to X. 
> 
> Before: ![Before Refactor](.\docs\images\CC_before_refactor.png)
> 
> After: ![After Refactor](.\docs\images\CC_after_refactor.png)
 

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

![Colour Check ](.\docs\images\CC_smiley_colour_check.png)
  ### Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

![Colour Check Blue Sad](.\docs\images\CC_blue_sad.png)
  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.
![Colour Check Yellow Happy](.\docs\images\CC_yellow_happy.png)
  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***

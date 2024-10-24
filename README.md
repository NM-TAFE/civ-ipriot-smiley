# Smiley: Intro to OOP and IoT
> :warning: This assessment may be distributed in one of the following forms:
> - **GitHub Classrooms**: You will automatically receive a  copy of this repo on NMTAFE's org (if you don't know what GitHub Classrooms is, then your group is not using it 😉)
> - **Blackboard**: There will be an assessment handout that may refer to parts or all of this repo
> 
> Both versions are otherwise identical and require answering the same questions and performing the same tasks.  

This assessment demonstrates your understanding of processes and techniques related to object-oriented programming, including the concepts and language. The assessment consists of a knowledge-based and practical component.

You begin with some starter code: A set of smiley faces that can be presented on a SenseHAT LED matrix (optional)

The project will help you demonstrate and cement your understanding of the four pillars of object-oriented programming:

1. **Abstraction**: expose objects in terms of how they are used, not how they are implemented
2. **Polymorphism**: handle different forms in the same way
3. **Inheritance**: by subclassing a common Smiley class
4. **Encapsulation**: protect the internal state of objects


## Working on this project

If using GitHub Classrooms, use the repository uniquely allocated to you. 
Otherwise,you **must** work against your forked version of this repository:

1. From the top-right corner, select **Fork** and follow the prompts.
2. Open the terminal (Command Prompt or Git Bash on Windows) and navigate to the desired parent folder for this project.
3. Clone the forked repository:

```bash

git clone https://github.com/YOUR_USERNAME/civ-ipriot-smiley.git
```

Replace `YOUR_USERNAME` with your GitHub username.

5. Navigate to the cloned repository:

```bash

cd civ-ipriot-smiley
```

6. Create a new branch:

```bash

git switch -c por2
```

7. Create a `venv` for your project:

```bash
python -m venv .venv
```

8. Open the project in PyCharm; the root folder should be `civ-ipriot-smiley`

9. Modify the code based on the [assessment requirements](knowledge_and_evidence.md)

---
**Recommended:**    
10. Stage the modifications you made:

```bash

git add .
```

9. Commit the changes:

```bash

git commit -m "Complete portfolio activity"
```

10. Push the changes:

```bash

git push -u origin por1
```

**End of recommended section**

11. Submit your work as per the assessment instructions on Blackboard. You can use GitHub to create a `zip` of your project if you followed the recommended steps previously.

------
### Oh fork: what to do if you didn't fork

> Also, what is a fork anyway?

A fork creates a personal copy of a repository on your own GitHub account.
What makes the fork a fork (rather than a plain old copy) is that the fork
still refers to the repository from whence it came as its `upstream`.

This still allows you to pull or push from the upstream.

At a conceptual level, a clone of a forked repository has your
copy of the repository as its `origin` with the origin's origin said to be 'upstream'.

If you cloned the original repository, and you want to keep the clone but
change it to use your copy:

1. Create a fork on GitHub and copy the name of your forked repository. Usually:
   `https://github.com/<YOUR_USERNAME>/civ-ipriot-smiley.git`
2. Go to your clone's local directory.
3. Run the following command to verify that your current clone is pointing
   at the NM-TAFE repo:

```bash
git remote -v
```

4. Change the origin to your upstream repository:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/civ-ipriot-smiley.git
```

Replace `YOUR_USERNAME` with, you guessed it, your GitHub username.

5. Add the original repository as the upstream:

```bash
git remote add upstream https://github.com/NM-TAFE/civ-ipriot-smiley.git
```

6. Optionally, you can fetch any changes that have been made to the original
   repository by running:

```bash
git fetch upstream
```

### After you have submitted

You may want to merge the changes back to your `main` branch using a pull request.

### Stretch goals

The following activities go beyond the project's basic requirements to teach us more modern software development principles. These activities should only be tried **after** you have met the project requirements, and they will not be assessed.

#### Favor composition over inheritance ('is a' versus 'has a')

While inheritance was one of the darlings of OOP, in modern software development, it is recognised that inheritance can introduce implicit dependencies (coupling) between various parts of the code. The famous adage captures this:

> Favour composition over inheritance

Raf's corollary to the above statement is:

> If there's some way to state a relationship in terms of `has a`, then that's probably the right way

We know what inheritance looks like:

```python
Parent:
   """Do common stuff"""

Child(Parent):
    """Do specialised stuff"""
```

But what does composition look like in Python?

Well, here's the crazy thing: you've already been doing composition; you just didn't know it. Let's go back to the very very first OOP example we did:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

Where's the composition?

That's right!

Remember, in Python, everything is an object!

So a dog **has a** `name` string and a dog **has a** `breed` string. Thus, a dog is **composed** of two strings: name and breed!

It is the same for any other object, including our own: when we create an instance of a class in another instance of the class, we are now composing one object from another.


##### Exercise

Reimagine the relationship between Smiley and Happy. How can we maintain reusability while _avoiding_ inheritance?

**Clues**

- "Happy `has a` Smiley?" doesn't sound right, does it?
- "Smiley `has a` Happy?" sounds even worse!
- What about a Smiley is composed of an Expression?
- What kind of class would Expression be?

##### Learn more

When we do use inheritance, we tend to favour inheriting from abstractions, not concrete classes. For example, it is pretty helpful to standardise everything that an "Expression" can do so that we can (polymorphically) handle expressions, so it makes sense for Happy, Sad, Etc, to inherit from Expression(ABC) and for Smiley to be composed of an expression (which we can pass at instantiation time).

[composition > inheritance](https://www.youtube.com/watch?v=hxGOiiR9ZKg)

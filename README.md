# Smiley: Intro to OOP and IoT

Demonstrates key Python OOP concepts and provides the first project's starting code.

The project presents various smiley faces that appear on the SenseHAT LED matrix.

The project helps students explore the core pillars of OOP. Specifically:

1. **Abstraction**: expose objects in terms of how they are used, not how they are implemented
2. **Polymorphism**: handle different forms in the same way
3. **Inheritance**: by subclassing a common Smiley class
4. **Encapsulation**: protect the internal state of objects

Students are encouraged to play around with the files to get a feel for what's going on.

## Working on this project

You **must** work against your forked version of this repository:

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

7. Modify the code based on the assessment requirements
8. Stage the modifications you made:

```bash

git add .
```

9. Commit the changes:

```bash

git commit -m "Addressed requirements of the porfolio"
```

10. Push the changes:

```bash

git push origin at2-part1
```

### Oh fork: what to do if you didn't fork

> Also, what is a fork anyway?

A fork creates a personal copy of a repository on your own github account.
What makes the fork a fork (rather than a plain old copy) is that the fork
still refers to the repository from whence it came as its `upstream`.

This allows you to still pull from the upstream or push from it.

At a technical level, a clone of a forked repository has your
copy of the repository as its `origin` and a reference to the forked
repository as `upstream`.

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

4. Change the origin to your personal upstream repository:

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

You may want to merge the changes back to your `main` branch.

### Stretch goals

The following are some activities that go beyond the project's basic requirements to teach us more modern software development principles. These activities should only be attempted **after** you have met the project requirements, and they will **not** be assessed.

#### Favor composition over inheritance ('is a' versus 'has a')

While inheritance was one of the darlings of OOP, in modern software development, it is recognised that inheritance can introduce implicit dependencies (coupling) between various parts of the code. This is captured by the famous adage:

> Favour composition over inheritance

Raf's corollary to the above statement is:

> If there's some way to state a relationship in terms of `has a`, then use a `has a` relationship.

We know what inheritance looks like:

```python
Parent:
   """Do common stuff"""

Child(Parent):
    """Do specialised stuff"""
```

But what does composition look like in Python?

Well, here's the crazy thing, you've already been doing composition, you just didn't know it. Let's go back to the very very first OOP example we did:

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

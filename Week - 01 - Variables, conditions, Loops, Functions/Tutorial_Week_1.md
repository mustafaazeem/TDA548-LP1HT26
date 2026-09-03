# Week 1 Tutorial: Python Foundations

## ILO

* **KU1:** Grasp the relation between source code, the interpreter, and the machine.
* **KU3:** Design algorithms to solve simple programming problems.
* **CS1:** Structure small programs by the use of concepts such as iterations, functions, modules, classes, and methods.
* **CS3:** Form readable, descriptive and well-documented program code.
* **CS6:** Build basic interactive programs with text-based (and graphical) user interfaces.
* **CS8:** Use programming tools such as text editor, command line interface, and IDE (integrated development environment).

## Objectives

After completing this tutorial, you should be able to:

1. Explain that Python source code is run by an interpreter, one instruction at a time.
2. Create and run a Python program that displays text using `print()`.
3. Store values in variables and use them in expressions and output.
4. Read text and integer input from a user using `input()` and `int()`.
5. Use an `if`/`else` statement to select between two actions.
6. Use a `for` loop and `range()` to repeat an instruction a fixed number of times.
7. Predict, run, and modify short Python programs to check your understanding.

# Lesson Plan 

We start with the idea that programming is giving precise instructions to a computer. We code together to get a few tiny programs running immediately. During this coding activity, we discuss as only that theory which is relevant and needed, avoiding overburdening ourselves with loads of theoratical aspects. 

A useful first lesson sequence:

1. **What a program does, control flow**
   - Show:
     ```python
     print("Hello, world!")
     ```
   - Change the text together and introduce multiple messages. Lets see that code is read top to bottom in a sequential way.

2. **Variables**
   - Present variables as named containers for values:
     ```python
     name = "Ada"
     age = 18
     print(name)
     print(age)
     ```
   - what do we predict the output to be (before running the program)?

3. **Input and output**
   - Make programs personal and interactive:
     ```python
     name = input("What is your name? ")
     print("Hello,", name)
     ```
   - Then type conversion:
     ```python
     age = int(input("How old are you? "))
     print("Next year you will be", age + 1)
     ```

4. **Conditions**
   - We discuss decisions through familiar rules:
     ```python
     temperature = int(input("Temperature: "))

     if temperature < 0:
         print("Wear a coat.")
     else:
         print("Normal weather.")
     ```

5. **Loops**
   - Start with repetition that are simply displayed, so that we can see:
     ```python
     for number in range(1, 6):
         print(number)
     ```
   - Then we make a simple task, such as adding five entered numbers.



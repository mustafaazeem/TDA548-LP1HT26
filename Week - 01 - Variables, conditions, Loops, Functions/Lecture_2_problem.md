# Week 1 - Lecture 2 - Problem: The Collatz Sequence

**_Note: You only need to read and understand the problem before the lecture. You are not required to produce a programming solution._** 

## ILO

* **KU1:** Grasp the relation between source code, the interpreter, and the machine.
* **KU3:** Design algorithms to solve simple programming problems.
* **CS1:** Structure small programs by the use of concepts such as iterations, functions, modules, classes, and methods.
* **CS3:** Form readable, descriptive and well-documented program code.
* **CS6:** Build basic interactive programs with text-based (and graphical) user interfaces.
* **CS8:** Use programming tools such as text editor, command line interface, and IDE (integrated development environment).

## Objectives

After completing this problem, you should be able to:

1. Explain how Python source code is executed by the interpreter.
2. Translate the even and odd properties into an algorithm.
3. Use variables, arithmetic expressions, and an `if`/`else` statement to calculate the next value in the sequence.
4. Use a loop to generate values until the sequence reaches `1`.
5. Define and call a function. 
6. Read input from the user and display the required output.
7. Write readable code with descriptive names, suitable formatting, and comments.
8. Run and check the program in a Python development environment using the provided example.

## Background

The Collatz sequence is defined as follows for any positive integer \(n\):

- If \(n\) is even, divide it by 2.
- If \(n\) is odd, multiply it by 3 and add 1.

Repeat this process until the value becomes 1.

For example, starting with 6 produces the sequence:

6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1

## Task

Write a program that:

1. Reads a positive integer from the user.
2. Uses a function to generate the Collatz sequence.
3. Prints each value in the sequence.
4. Prints the total number of steps required to reach 1.

## Example Run

```text
Enter a positive integer: 6

6
3
10
5
16
8
4
2
1

Number of steps: 8
```

## Requirements

- Use at least one function.
- Use a loop to generate the sequence.
- Assume the user enters a positive integer.
``
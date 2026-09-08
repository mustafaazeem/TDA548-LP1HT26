# Week 2 - Lecture 4 - Problem: Message Organizer

**_Note: You only need to read and understand the problem before the lecture. You are not required to produce a programming solution._**

## ILO

* **KU1:** Grasp the relation between source code, the interpreter, and the machine.
* **KU2:** Choose appropriate data types and data structures for different kinds of data, depending on their performance characteristics.
* **KU3:** Design algorithms to solve simple programming problems.
* **CS1:** Structure small programs by the use of iterations, functions, modules, classes, and methods.
* **CS3:** Form readable, descriptive and well-documented program code.
* **CS5:** Express mathematical formulas as programming language expressions and algorithms.
* **CS6:** Build basic interactive programs with text-based and graphical user interfaces.
* **CS8:** Use programming tools such as text editor, command line interface, and IDE.
* **CS9:** Use standard libraries and follow best programming practices.

## Objectives

After completing this problem, you should be able to:

1. Store and manipulate text using strings and string methods.
2. Split a message into a list of words.
3. Use indexing and slicing to inspect parts of a string or list.
4. Use a tuple to store a fixed summary of message information.
5. Change a list in place using a list method.
6. Pass a named argument to a function.
7. Encode a string as UTF-8 bytes and decode it back into a string.
8. Write readable code with descriptive names and suitable formatting.

## Background

Messaging systems often prepare text before displaying or storing it. A program may need to clean a message, count its words, show a preview, and check how it is represented when sent over a network.

In this problem, you will create a small message organizer. The program receives one message and produces a cleaned version, a list of its words, a short preview, and information about its UTF-8 encoding.

A string is an immutable sequence of characters. This means that string methods create a new string rather than changing the original string. A list is mutable, so its contents can be changed in place.

## Task

Write a program that:

1. Reads a message from the user.
2. Removes unnecessary whitespace from the beginning and end of the message.
3. Splits the cleaned message into a list of words.
4. Sorts the list of words in place, ignoring letter case.
5. Replaces the first word in the sorted list with its uppercase version.
6. Creates a tuple containing:
   - the number of words,
   - the first word after the replacement, and
   - the last word in the message.
7. Creates a preview containing the first three words, or all words if the message has fewer than three words.
8. Encodes the cleaned message using UTF-8.
9. Decodes the bytes back into a string.
10. Prints the results.

Use a function with a named argument to create the preview. For example, the function may have a parameter named `limit`, and the function call should pass the argument by name.

Use a list method such as `.sort()` or `.reverse()` to change a list in place. The program should make clear that this operation changes the list itself.

## Example Run

```text
Enter a message:   Meet me at the café tomorrow   

Cleaned message: Meet me at the café tomorrow
Words: ['AT', 'café', 'me', 'Meet', 'the', 'tomorrow']
Message summary: (6, 'AT', 'tomorrow')
Preview: AT café me
UTF-8 bytes: b'Meet me at the caf\xc3\xa9 tomorrow'
Decoded message: Meet me at the café tomorrow
```

## Requirements

- Use at least one function for part of the processing.
- Use string methods such as `.strip()`, `.upper()`, and `.split()`.
- Use a list to store the words and sort it in place with a list method.
- Use indexing to access the first and last words.
- Use slicing to create the preview.
- Use a tuple for the message summary.
- Use a named argument when calling the preview function.
- Use `.encode("utf-8")` and `.decode("utf-8")`.
- Assume that the user enters a message containing at least one word.

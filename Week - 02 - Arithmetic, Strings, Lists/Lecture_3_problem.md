# Week 2 - Lecture 3 - Problem: Shape Area Calculator

**_Note: You only need to read and understand the problem before the lecture. You are not required to produce a programming solution._**

## ILO

* **KU3:** Design algorithms to solve simple programming problems.
* **CS1:** Structure small programs by the use of concepts such as iterations, functions, modules, classes, and methods.
* **CS3:** Form readable, descriptive and well-documented program code.
* **CS5:** Express mathematical formulas as programming language expressions and algorithms.
* **CS6:** Build basic interactive programs with text-based and graphical user interfaces.
* **CS9:** Use standard libraries and follow best programming practices.

## Objectives

After completing this problem, you should be able to:

1. Use functions to calculate the area of different shapes.
2. Use `float()` to read measurements from the user.
3. Use the `math` library and the predefined constant `math.pi`.
4. Use a loop to present a menu until the user chooses to quit.
5. Compare two floating-point areas using `math.isclose()` rather than `==`.
6. Format floating-point results with two decimal places.
7. Write readable code with descriptive names and suitable formatting.

## Related Self Practice sections 
* Variables, Loops, Functions 
* Floating point 

## Background

Several real-life situations require area calculation, for example when estimating:

* paint for a wall,
* material for a triangular road sign, or
* metal needed for a cylindrical container.

Some of the popular area calculation formulas for various shapes are:

$$
\begin{aligned}
\text{Square:} &\quad A = s^2 \\
\text{Rectangle:} &\quad A = w \cdot h \\
\text{Triangle:} &\quad A = \frac{b \cdot h}{2} \\
\text{Circle:} &\quad A = \pi r^2 \\
\text{Cylinder surface area:} &\quad A = 2\pi rh + 2\pi r^2
\end{aligned}
$$

Moreover, comparing areas of different shapes may be needed in certain cases. Some examples include deciding which sign is larger, which container has a larger surface, or which shape requires more material. 

Because Python stores floating-point values as approximations, two values that should be equal may not be exactly equal when compared with `==`. Therefore, use `math.isclose()` to compare floating-point areas reliably.

## Task

Write a menu-driven program with the following options:

1. Calculate the area of a square.
2. Calculate the area of a rectangle.
3. Calculate the area of a triangle.
4. Calculate the area of a circle.
5. Calculate the surface area of a cylinder.
6. Compare the areas of two shapes.
7. Quit the program.

When the user chooses a shape, ask for the measurements needed by its formula and print the calculated area. The shape options should call the corresponding area functions directly.

When the user chooses the comparison option, ask them to choose two shapes from the same shape menu. Then ask for their measurements and calculate both areas.

When comparing two shapes, print whether the areas are approximately equal. Otherwise, state which shape has the larger area.

Keep showing the main menu until the user selects the quit option. If the user enters an invalid menu choice, show an error message and display the menu again.

## Example Run

```text
Shape Area Calculator
1. Calculate square area
2. Calculate rectangle area
3. Calculate triangle area
4. Calculate circle area
5. Calculate cylinder surface area
6. Compare two shapes
7. Quit
Choose an option: 6

Choose the first shape: 2
Width: 5
Height: 5.65
Area of the rectangle: 28.25

Choose the second shape: 4
Radius: 3
Area of the circle: 28.27

The areas are approximately equal.
```

## Requirements

- Define a separate function for each shape's area calculation.
- Import and use math library for needed constants.
- Compare area of shapes with reliable means 
- Display every calculated area with two decimal places.
- Use a loop to keep the main menu running until the user quits.
- Use a loop to validate menu choices.
- Assume all entered shape measurements are positive.

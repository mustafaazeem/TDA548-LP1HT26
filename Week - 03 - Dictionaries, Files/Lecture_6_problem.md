# Week 3 - Lecture 6 - Problem: Weather Station Data Stream

## ILO

* **KU2:** Choose appropriate data types and data structures for different kinds of data.
* **KU3:** Design algorithms to solve simple programming problems.
* **CS1:** Structure small programs using iterations, functions, and generators.
* **CS3:** Write readable, descriptive, and well-documented program code.
* **CS9:** Use standard libraries and follow good programming practices.

## Objectives

After completing this problem, you should be able to:

1. Validate data before converting or processing it.
2. Distinguish malformed records from values outside an allowed range.
3. Use `try` and `except` to handle conversion errors.
4. Write a generator function using `yield`.
5. Read and process one record at a time.
6. Build a generator that filters a data stream.
7. Stop a search as soon as the required result is found.
8. Explain why a generator is useful for a large or continuous data source.

## Background

A weather station sends measurements continuously. Each measurement contains a time, a temperature, and a humidity value. The data arrives as text records in the following format:

```text
time;temperature;humidity
```

For example:

```text
08:00;12.5;86
08:10;13.1;74
08:20;bad;73
08:30;14.0;105
08:40;15.2;70
```

Some records may be invalid. A record is valid when:

- it has exactly three fields;
- the time is not empty;
- the temperature is a number between `-50` and `60` degrees Celsius; and
- the humidity is an integer between `0` and `100` percent.

The program should process the readings as a stream. It should not first create a second list containing all valid readings. A generator should yield each valid reading when it is needed.

## Task

### Part 1: Validate one record

Write a function `parse_reading(line)` that receives one line of text.

The function should:

1. Remove the newline and surrounding whitespace.
2. Split the line into fields using `;`.
3. Reject the line if it does not contain exactly three fields.
4. Convert temperature to a `float` and humidity to an `int`.
5. Reject the line if either conversion raises `ValueError`.
6. Reject values outside the allowed ranges.
7. Return a tuple `(time, temperature, humidity)` for a valid line.
8. Return `None` for an invalid line.

Example:

```python
parse_reading("08:00;12.5;76")
# ('08:00', 12.5, 76)

parse_reading("08:20;bad;73")
# None
```

Do not let an invalid record crash the program.

### Part 2: Generate valid readings

Write a generator function `valid_readings(lines)` that receives an iterable of text lines and yields only valid readings:

```python
def valid_readings(lines):
    for line in lines:
        reading = parse_reading(line)
        if reading is not None:
            yield reading
```

Test it with this data:

```python
data = [
    "08:00;12.5;86",
    "08:10;13.1;74",
    "08:20;bad;73",
    "08:30;14.0;105",
    "08:40;15.2;70"
]

for reading in valid_readings(data):
    print(reading)
```

Expected output:

```text
('08:00', 12.5, 86)
('08:10', 13.1, 74)
('08:40', 15.2, 70)
```

The invalid records are skipped, but the generator does not need to build a separate list of valid records.

### Part 3: Generate alerts

Write a second generator `humidity_alerts(readings)` that receives an iterable of valid readings and yields only readings where the humidity is at least 80:

```python
def humidity_alerts(readings):
    for time, temperature, humidity in readings:
        if humidity >= 80:
            yield time, temperature, humidity
```

Use the generators together:

```python
for reading in humidity_alerts(valid_readings(data)):
    print("High humidity:", reading)
```

This is a generator pipeline: the data passes through one stage at a time.

### Part 4: Find the first cold reading

Write a function `first_below(readings, limit)` that returns the first reading whose temperature is below `limit`.

Return `None` if no reading matches. Stop immediately when a matching reading is found; do not process the remaining readings.

Example:

```python
first_below(valid_readings(data), 14)
# ('08:00', 12.5, 76)
```

Explain why returning immediately is useful when `readings` is a generator or when the data source is very large.

### Part 5: Read from a file

Create a file called `weather.txt` with the following contents:

```text
08:00;12.5;86
08:10;13.1;74
08:20;bad;73
08:30;14.0;105
08:40;15.2;70
```

Use the file itself as the input to the generator:

```python
with open("weather.txt", "r") as file:
    for reading in valid_readings(file):
        print(reading)
```

The file can be processed one line at a time. The complete file does not need to be loaded into a separate list first.

## Example Run

```text
Valid readings:
08:00: 12.5 C, humidity 86%
08:10: 13.1 C, humidity 74%
08:40: 15.2 C, humidity 70%

High humidity readings:
08:00: 12.5 C, humidity 86%

First reading below 14 C:
08:00: 12.5 C, humidity 86%
```

## Requirements

- Validate each record before using its values.
- Reject records with the wrong number of fields.
- Catch `ValueError` when converting temperature or humidity.
- Reject temperatures outside `-50` to `60` degrees Celsius.
- Reject humidity outside `0` to `100` percent.
- Return `None` for invalid records instead of crashing.
- Use at least two generator functions containing `yield`.
- Process valid readings one at a time.
- Use a generator pipeline for the humidity alerts.
- Stop `first_below()` as soon as a matching reading is found.
- Process the file directly instead of first calling `readlines()`.
- Do not use a bare `except:`.

## Discussion Questions

1. What is the difference between `return` and `yield`?
2. When does the body of a generator function begin running?
3. Why can `valid_readings(file)` process a large file efficiently?
4. Why can a generator normally be consumed only once?
5. What is the difference between a malformed record and an out-of-range value?
6. Why should `parse_reading()` return `None` for an invalid record?
7. Why should `first_below()` return immediately after finding a match?

## Extension Challenges

1. Add a wind-speed field and validate it as a non-negative number.
2. Write a generator that yields only readings from a selected time interval.
3. Write a generator that yields the running average temperature.
4. Write a generator that yields a warning when the temperature changes by more than 5 degrees between consecutive valid readings.
5. Count invalid records without storing them.
6. Write valid readings to a new output file while the input file is processed.

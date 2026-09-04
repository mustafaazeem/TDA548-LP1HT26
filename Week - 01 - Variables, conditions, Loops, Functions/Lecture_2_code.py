'''
Generate a Collatz sequence for a positive integer.

This solution is not from live coding in the lecture. What we coded in lecture
is given below. This solution is a neat version'''

def generate_collatz_sequence(number: int) -> int:
    """Print the Collatz sequence and return the number of steps."""
    steps = 0
    print(number)

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

        print(number)
        steps += 1

    return steps


number = int(input("Enter a positive integer: "))
steps = generate_collatz_sequence(number)
print()
print("Number of steps:", steps)


''' 
Below this is the code which we wrote in class. 
We modified it several times to show different aspects, so this code may not 
make sense to you. But as promised, I upload it 

'''
# Input 


# Algorithm: Now we put it into a function 
# Function definition 
# def gen_collatz_seq(number: int):    # function header / signature 

#     # function body 
#     while number != 1:
#         if number%2:
#             number = (number * 3) + 1
            
#         else:
#             number = int(number / 2)
            

#         # Output 
#         print(number)   



# input validation 
# while True:
#     number = int(input("Enter a +ive int, (0 to exit): ")) 
#     if number == 0:
#         break
#     elif number < 0:
#         print("You int is -ive, only +ive int are allowed")
#         continue
#     if number > 0:
#         print("You entered correct input")
#         break 


# if number > 0: 
#     gen_collatz_seq(number)     # Function call 

# elif number < 1:
#     print("You entered a wrong input")

# else: 
#     print("Only positive integers are allowed")


# def function_name (What will be the input):
    # algorithm here 
    # return some output from this function 

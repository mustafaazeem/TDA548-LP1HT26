# def functiona_name (inputs)
# def find_quadratic_roots(paramters):
#     # write your quadratic formula solution here 

import math     # math module 
# we have written the value of pi in math module

def calculate_square_area(length):
    '''
    ( This comment is called a docstring ) 
    This function calculates area of a square.
    Input: it takes length of a side 
    Output: It returns the area 
    '''
    area = pow(length, 2)

    return area 

def calculate_rectangle_area(width, height):
    '''
    This function calculates area of a rectangle
    '''
    return width * height 

def calculate_triangle_area(base, height):
    return base * height / 2 

def calculate_circle_area(radius):
    return 2 * math.pi * radius 

def UI():
    while True:
        print("Dear user: Please choose which shape area you want to calculate: ")
        print(" Shape Area Calculator\n" \
            "1. Calculate square area\n" \
            "2. Calculate rectangle area\n" \
            "3. Calculate triangle area\n" \
            "4. Calculate circle area\n" \
            "5. Calculate cylinder surface area\n" \
            "6. Compare two shapes\n" \
            "7. Quit")
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            side = float(input("Enter side measurement: "))
            area = calculate_square_area(side)
            print(f'Area of square is {area}')

        elif user_choice == 2:
            pass

        elif user_choice == 7:
            break

def UI2():
    while True:
        print(" Shape Area Calculator\n" \
        "1. Calculate square area\n" \
        "2. Calculate rectangle area\n" \
        "3. Calculate triangle area\n" \
        "4. Calculate circle area\n" \
        "5. Calculate cylinder surface area\n" \
        "6. Compare two shapes\n" \
        "7. Quit")

        area = 0.0 

        choice = int(input("Please enter your choice: "))

        if choice == 7:
            break
        elif choice == 6:
            radius = float(input("Enter radius: "))
            circle_area = calculate_circle_area(radius)

            base = float (input("Enter base: "))
            height = float (input("Enter height: "))
            triangle_area = calculate_triangle_area(base, height)

            if circle_area == triangle_area:
                print(f"Both shapes have same area {circle_area} and {triangle_area}")
            else:
                print("Both shapes have different area")

        elif choice == 5:
            pass
        elif choice == 4:
            radius = float(input("Enter radius: "))
            area = calculate_circle_area(radius)
        elif choice == 3:
            base = float (input("Enter base: "))
            height = float (input("Enter height: "))
            area = calculate_triangle_area(base, height)
        elif choice == 2:
            width = float (input("Enter width: "))
            height = float (input("Enter height: "))
            area = calculate_rectangle_area(width, height)
        elif choice == 1:
            side = float (input ("Enter side length: "))
            area = calculate_square_area
        else:
            print(f"You have entered an incorrect choice {choice}: Please try again")

        print(f'The area of your shape is {area:.3f}')

UI()

# area = calculate_rectangle_area(width, height)
# print(area)




# length = float(input("Enter length: "))

# area = calculate_square_area(length)
# print("The area is:", area, " cm^2")
# # area = round(area, 3)
# print(area)
# print(f"The rounded area is {area:.2f} cm^2" )
# print(area)
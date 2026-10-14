# Exam question 1: 2026 - June 

# xn_1 = (a * xn) - (b * xn * yn)
# yn_1 = -(g * yn) + (d * xn * yn)

import math 

def next_generation(a, b, g, d, xn, yn):
    xn_1 = max(0, (a * xn) - (b * xn * yn))
    yn_1 = max(0, -(g * yn) + (d * xn * yn))

    return xn_1, yn_1

def evolution():
    xn = int(input("Rabbit population: "))
    yn = int(input("Wolf population: "))
    n = int(input("Number of generations: "))

    a, b, g, d = 5, 0.01, 0.4, 0.01 

    for _ in range(n):
        # xn_1, yn_1 = next_generation(a, b, g, d, xn, yn)        
        # print(f'{xn_1:.0f} {yn_1:.0f}')
        # xn, yn = xn_1, yn_1

        xn, yn = next_generation(a, b, g, d, xn, yn)
        print(f'{math.floor(xn)} {math.floor(yn)}')

evolution()






# print(next_generation(5,0.01,0.4,0.01,150,10))
# print(next_generation(1.1,0.1,0.1,1.2,70,25))
# print(next_generation(1.1,0.1,2,0.01,30,10))
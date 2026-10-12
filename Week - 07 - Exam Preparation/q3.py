######################## Q1 2608

# gc-content = 100 * (g+c) / (a+t+g+c)

# at-gc = (a+t) / (g+c)

def dna_content():
    allowed = {'G', 'C', 'A', 'T'}
    # seq = input("DNA sequence: ")
    seq = 'GCGCAAATTT'
    # seq = 'GCGCaAATTT'
    # seq = 'ATXCC'
    # seq = 'AAATTATTTT'
    # seq = ''

    a = seq.count('A')
    t = seq.count('T')
    g = seq.count('G')
    c = seq.count('C')

    if not seq:
        print('Empty sequence')
    elif a+t+g+c != len(seq):
        print("Invalid sequence")
    elif g+c == 0:
        print("No G or C")
    else:
        gc_content = 100 * (g+c) / (a+t+g+c)
        at_gc = (a+t) / (g+c)
        print(f'GC-content {gc_content}')
        print(f'AT-GC ratio {at_gc}')

    # gc = 0

    # if not seq:
    #     print('Empty sequence')
    # else:
    #     for n in seq:
    #         if n == 'G' or n == 'C':
    #             gc += 1
    #         elif n == 'A' or n == 'T':


    # if not seq:
    #     print("Empty sequence")
    #     # return 

    # # elif any(n not in allowed for n in seq):
    # elif [0  for n in seq if n not in allowed]:    
    #     print("Invalid sequence")
    #     # return 

    # elif 'G' not in seq and 'C' not in seq:
    #     print("No G or C")
    #     # return

    # else: 
    #     g = seq.count('G')
    #     c = seq.count('C')
    #     a = seq.count('A')
    #     t = seq.count('T')    
    #     gc_content = 100 * (g+c) / (a+t+g+c)
    #     at_gc = (a+t) / (g+c)

    #     print(f'GC-content: {gc_content}')
    #     print(f'AT-GC ratio: {at_gc}')
    

# dna_content()

######################## Q1 2606

def next_generation(a, b, g, d, xn, yn):
    xn_1 = max(0, (a*xn) - (b*xn*yn))
    yn_1 = max(0, -(g*yn) + (d*xn*yn))
    return xn_1, yn_1

# print(next_generation(5,0.01,0.4,0.01,150,10))
# print(next_generation(1.1,0.1,0.1,1.2,70,25))
# print(next_generation(1.1,0.1,2,0.01,30,10))

import math 
def evolution():
    # r_pop = int(input("Rabbit population: "))
    # w_pop = int(input("Wolf population: "))
    # gens = int(input("Number of generations"))

    xn = 130
    yn = 7
    gens = 4
    a, b, g, d = 5, 0.01, 0.4, 0.01 

    # xn_1, yn_1 = 0
    
    for gen in range(gens):
        xn, yn = next_generation(a, b, g, d, xn, yn)
        print(f'{math.floor(xn)} {math.floor(yn)}')

    

# evolution()

######################## Q2 2606

def runs(l):
    if not l:
        return []
    
    runs_list = []
    current = l[0]
    count = 1

    for next in l[1:]:
        if next == current:
            count += 1
        else:
            runs_list.append((count, current))
            current = next
            count = 1

    runs_list.append((count, current))

    return runs_list


# runs([True, True, True, True, False, False, False]) == [(4, True), (3, False)]

# runs(list("mississippi")) == [(1,'m'),(1,'i'),(2,'s'),(1,'i'),(2,'s'),(1,'i'),(2,'p'),(1,'i')]

runs_list = runs(list("mississippi"))
print(runs_list)

def expand(r):
    l = []
    for count, ch in r:
        # print(count, ch)
        l.extend([ch]*count)
    return l

print(expand(runs_list))




class Station:
    pass
# Exam question 2: 2026 - June 

def runs(l):
    runs_list = []

    current = l[0]
    count = 1

    for x in l[1:]:
        if x == current:
        # that means the same character is at
        # the next position also, therefore 
        # I simply increase my count 
            count += 1

        else:
        # The next character x is not same
        # as the current character 
            runs_list.append( (count, current) )
            current = x
            count = 1
    runs_list.append( (count, current) )
    return runs_list



def expand(r):
    l = []
    for count, char in r:
        l.extend( [char]*count )
    return l

r = [(1, 'm'), (1, 'i'), (2, 's'), (1, 'i'), (2, 's'), (1, 'i'), (2, 'p'), (1, 'i')]

print(expand(r))

# [m,i,s,s,i,s,s,i,p,p,i]

# print(runs([True, True, True, True, False, False, False]))
# # [(4, True), (3, False)]
# print(runs(list("mississippi")))
# # [(1,'m'),(1,'i'),(2,'s'),(1,'i'),(2,'s'),(1,'i'), (2,'p'),(1,'i')]
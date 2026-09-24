import math 
G = 6.674e-11

def escape(M, r, V):
    '''
    V is leaving object's velocity 
    M is planet's mass 
    r is planet's radius
    calculate v
    v is escape velocity 
    ei s excess speed '''

    v = (2*G*M / r)**0.5

    # e = math.sqrt(-5) 
    e = (V**2 - v**2)**0.5
    

    if V > v:
        e = math.sqrt(V**2 - v**2)
        print(f'Excess speed: {e}')
    else:
        print("The object won't escape")

escape(7.3e22, 1.7e6, 5000)
escape(6e24, 5.6e6, 5000)
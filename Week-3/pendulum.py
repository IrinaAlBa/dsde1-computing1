import math
def period(L,g):
    x = isinstance(L, int)
    if x == False:
        raise Exception("There is something wrong here...")
    y = isinstance(g, int)
    if y == False:
        raise Exception("There is something wrong here...")
    print(x)
    print(y)
    T = 2*math.pi*((L/g)**(1/2))
    print(T)

period(10,5)
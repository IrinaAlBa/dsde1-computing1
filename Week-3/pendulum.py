<<<<<<< HEAD

=======
>>>>>>> 691fe0e9aa6d00e67394590d08fc44ab8982d327
import math
def period(L,g):
    x = isinstance(L, (int,float))
    if not x:
        raise TypeError("L must be a number")
    y = isinstance(g, (int,float))
    if not y:
        raise TypeError("g must be a number")
    if L<= 0:
        raise ValueError("L must be positive")
    y = isinstance(g, (int,float))
    if g<= 0:
        raise ValueError("g must be positive")
    T = 2*math.pi*((L/g)**(1/2))
    print(f'{T:.2f}')
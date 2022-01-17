from math import sqrt


def find_roots(a, b, c):
    det = b**2 - (4*a*c)

    #Since it is assumed in the question that the quadratic equation has at least one real solution we need not consider imaginary solutions

    if det==0: #only one real solution
        res = -b / (2*a)
        return (res,res) #Returns the solution as a tuple

    if det > 0: #two real and distinct solutions
        res1 = (-b + sqrt(det)) / (2*a)
        res2 = (-b - sqrt(det)) / (2*a)
        return (res1,res2)

    if det<0: #case were solution is imaginary
        return (None,None)

print("Enter co-efficients a,b and c for the quadratic equation ax^2 + bx + c = 0:")
a,b,c = map(int,input().split())
res1,res2 = find_roots(a,b,c)

print(f"The roots of the quadratic equation are {res1} and {res2}")
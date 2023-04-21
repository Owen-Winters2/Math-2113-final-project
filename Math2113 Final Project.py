import numpy as np
import math 

def strC(x):
    s = ""
    if(abs(x.real) > 0.001):
        s = s + str("{:.3f}".format(x.real))
    if(abs(x.imag) > 0.001):
        if(abs(x.real) > 0.001):
            s = s + " + "
        s = s + str("{:.3f}".format(x.imag)) + "j"
    if(s == ""):
        s = "0"
    if(abs(x.real) > 0.001 and abs(x.imag) > 0.001):
        s = "(" + s + ")"
    return s
    

print("s(n+2) = as(n+1) + bs(n) + cn + d \nEnter values of recurence relation")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

res0 = float(input("Real component of s0: "))
ims0 = float(input("Complex component of s0: "))
if(ims0 == 0):
    s0 = res0
else:
    s0 = complex(res0, ims0)

res1 = float(input("Real component of s1: "))
ims1 = float(input("Complex component of s1: "))
if(ims1 == 0):
    s1 = res1
else:
    s1 = complex(res1, ims1)

determ = a ** 2 + 4 * b

if(determ < 0):
    alph = complex(a/2.0, math.sqrt(-determ) / 2)
    beta = complex(a/2.0, -math.sqrt(-determ) / 2)
else:
    alph = (a + math.sqrt(determ)) / 2
    beta = (a - math.sqrt(determ)) / 2
    
a1 = c + s1 - a * s0 - d
a2 = s0 - 2 * s1 + 2 * a * s0 + d
a3 = -2 * s0 + s1 - a * s0
a4 = s0

firstPr = False


if(a1 == 0):
    a1Gen = ""
else:
    a1Gen = str(a1) + "x^3 "
    firstPr = True
if(a2 == 0):
    a2Gen = ""
else:
    if(not firstPr):
        a2Gen = str(a2) + "x^2 "
    else:
        a2Gen = "+ " + str(a2) + "x^2 "
    firstPr = True        
if(a3 == 0):
    a3Gen = ""
else:
    if(not firstPr):
        a3Gen = str(a3) + "x "
    else:
        a3Gen = "+ " + str(a3) + "x "
    firstPr = True
if(a4 == 0):
    a4Gen = ""
else:
    if(not firstPr):
        a4Gen = str(a4)
    else:
        a4Gen = "+ " + str(a4)

alphGen = "(1 - " + strC(alph) + "x)"
betaGen = "(1 - " + strC(beta) + "x)"

B = np.zeros(4, dtype = "complex_")
A = np.array([a1, a2, a3, a4])

print("\nThe generating function is: \n")
print("\u0332".join( "(" + a1Gen + a2Gen + a3Gen + a4Gen + ")"))
print(alphGen + betaGen + "(1 - x)^2\n")



if(alph != beta and alph != 1 and beta != 1):
    
    X = np.array([[-beta, -alph, b, 0],[2 * beta + 1, 2 * alph + 1, a - b, -b],[-beta - 2, -alph - 2, -a-1, -a],[1,1,1,1]])
    B = np.linalg.solve(X, A)

    B1 = strC(B[0]) + "(" + strC(alph) + ")^n + "
    B2 = strC(B[1]) + "(" + strC(beta) + ")^n + "
    B3 = strC(B[2] + B[3]) + " + "
    B4 = strC(B[3]) + "n"

    print("sn = " + B1 + B2 + B3 + B4 + "\n")

    i = 0
    while(i < 10):
        print("s" + str(i) + " = " + strC(B[0] * alph ** i + B[1] * beta ** i + B[2] + B[3] * (i + 1)))
        i = i + 1
    print("Enter any value of n you want to check. To stop, enter a negative integer.")
    i = int(input("n = "))
    while(i > -1):
        print("s" + str(i) + "=" + strC(B[0] * alph ** i + B[1] * beta ** i + B[2] + B[3] * (i + 1)))
        i = int(input("n = "))
        
elif(alph == beta and alph != 1):
    X = np.array([[-alph,0,b,0],[1 + 2 * alph, 1, a-b, -b],[-2-alph, -2, -a-1, -a],[1,1,1,1]])
    B = np.linalg.solve(X, A)

    B1 = "(" + strC(B[0] + B[1]) + ")(" + strC(alph) + ")^n + "
    B2 = "(" + strC(B[1]) + ")(n)(" + strC(beta) + ")^n + "
    B3 = strC(B[2] + B[3]) + " + "
    B4 = strC(B[3]) + "n"

    print("sn = " + B1 + B2 + B3 + B4 + "\n")

    i = 0
    while(i < 10):
        print("s" + str(i) + " = " + strC(B[0] * alph ** i + B[1] * (i + 1) * alph ** i + B[2] + B[3] * (i + 1)))
        i = i + 1
    print("Enter any value of n you want to check. To stop, enter a negative integer.")
    i = int(input("n = "))
    while(i > -1):
        print("s" + str(i) + " = " + strC(B[0] * alph ** i + B[1] * (i + 1) * alph ** i + B[2] + B[3] * (i + 1)))
        i = int(input("n = "))
        
elif(alph != beta and (alph == 1 or beta ==1)):

    if(beta != 1):
        alph = beta
    
    X = np.array([[-1, -alph, 0, 0],[3,2 * alph + 1, alph, 0],[-3, -alph -2, -alph - 1, -alph],[1,1,1,1]])
    B = np.linalg.solve(X, A)

    B1 = strC(B[0]) + "(" + strC(alph) + ")^n + "
    B2 = strC(B[1] + B[2] + B[3]) + " + "
    B3 = strC(B[2] + 3 / 2 * B[3]) + "n + "
    B4 = strC(1 / 2 * B[3]) + "n^2"

    print("sn = " + B1 + B2 + B3 + B4 + "\n")

    i = 0
    while(i < 10):
        print("s" + str(i) + " = " + strC(B[0] * alph ** i + B[1] + B[2] * (1 + i) + B[3] * 1 / 2 *(i + 1) * (i + 2)))
        i = i + 1
    print("Enter any value of n you want to check. To stop, enter a negative integer.")
    i = int(input("n = "))
    while(i > -1):
        print("s" + str(i) + " = " + strC(B[0] * alph ** i + B[1] + B[2] * (1 + i) + B[3] * (i + 1) * (i + 2) / 2))
        i = int(input("n = "))

elif(alph == beta and alph == 1):
    
    X = np.array([[-1,0,0,0],[3,1,0,0],[-3,-2,-1,0],[1,1,1,1]])
    B = np.linalg.solve(X, A)

    B1 = strC(B[0]+B[1]+B[2]+B[3]) + " + "
    B2 = strC(B[1] + 3 / 2 * B[2] + 11/6 * B[3]) + "n + "
    B3 = strC(1 / 2 * B[2] + B[3]) + "n^2 + "
    B4 = strC(1 / 6 * B[3]) + "n^3"

    print("sn = " + B1 + B2 + B3 + B4 + "\n")

    i = 0
    while(i < 10):
        print("s" + str(i) + " = " + strC(B[0] + B[1] +B[2]+B[3] +(B[1] + 3 / 2 * B[2] + 11/6 * B[3]) * i + (1 / 2 * B[2] + B[3]) * i ** 2 + (1/ 6 * B[3]) * i ** 3))
        i = i + 1
    print("Enter any value of n you want to check. To stop, enter a negative integer.")
    i = int(input("n = "))
    while(i > -1):
        print("s" + str(i) + " = " + strC(B[0] + B[1] +B[2]+B[3] +(B[1] + 3 / 2 * B[2] + 11/6 * B[3]) * i + (1 / 2 * B[2] + B[3]) * i ** 2 + (1/ 6 * B[3]) * i ** 3))
        i = int(input("n = "))
        

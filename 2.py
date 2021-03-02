import math
import random

p = int(input("Δώσε έναν αριθμό της ακολουθίας Fibonacci:"))

#ελεγχος εαν ενας αριθμος ειναι τελειο τετράγωνο

def tetragwno(x):
    y= int(math.sqrt(x))
    return y*y==x

#ελεγχος εαν ενας αριθμος ανήκει στην ακολουθία (true εαν ειναι, false εαν οχι)

def  fibonacci(u):
    #ένας αριθμος ανηκει στην ακολουθια εαν ειναι τελειο τετραγωνο και ισχυει (5*u*u+4) ή (5*u*u-4)
    return tetragwno(5*u*u+4) or tetragwno(5*u*u-4)

randoma=[]
for i in range(0,19):
    randoma.append(random.randint(-10000000000,10000000000))

#εαν το message είναι true, o αριθμος είναι πρωτος και ανηκει στην ακολουθία, εάν false δεν είναι πρώτος ή/και δεν ανήκει στην ακολουθία

message=True

if fibonacci(p)==True and p>0:
    for a in range(0,19):
        if (randoma[a]**p)%p != randoma[a]%p:
            message=False
else:
    print("Ο αριθμός που έδωσες δεν ανήκει στην ακολουθία.")
            

if fibonacci(p)==True and p>0:
    if message==True:
        print("Το "+str(p)+ " είναι ένας πρώτος αριθμός από την ακολουθία Fibonacci!")
    else:
        print("Ο αριθμός που έδωσες δεν είναι πρώτος")
    



    

from algorithms import *
from cocomax import *
import time
import matplotlib.pyplot as plt

Nmin = 4
Nmax = 6
print("Q1 : How many allocations are generated by each algorithm on average?")

#generation de couples de profils rapides jusqu'a N = 12
RS_values = list()
OS_values = list()
BU_values = list()
TR_values = list()

for N in range(Nmin, Nmax+1, 2):
    L_C = L_couple_single_peaked_preferences(N)
    print("Number of problems : {}".format(len(L_C)))



    OS_Number_of_allocations_L = list()
    for profile_A, profile_B in L_C:
        U = {i for i in range(1, N+1)}
        Allocations = OS(Alloc=list(), Z_A=set(), Z_B=set(), A_pprofile=profile_A, B_pprofile=profile_B, U=U)
        nb = len(Allocations)
        if nb != 0:
            OS_Number_of_allocations_L.append(nb)

    OS_values.append(1.*sum(OS_Number_of_allocations_L)/len(OS_Number_of_allocations_L))

    RS_Number_of_allocations_L = list()
    for profile_A, profile_B in L_C:
        U = {i for i in range(1, N+1)}
        Allocations = RS(Alloc=list(), Z_A=set(), Z_B=set(), A_pprofile=profile_A, B_pprofile=profile_B, U=U)
        nb = len(Allocations)
        if nb != 0:
            RS_Number_of_allocations_L.append(nb)

    RS_values.append(1.*sum(RS_Number_of_allocations_L)/len(RS_Number_of_allocations_L))


    BU_Number_of_allocations_L = list()
    for profile_A, profile_B in L_C:
        Allocations = BU(N=N, A_pprofile=profile_A, B_pprofile=profile_B)
        nb = len(Allocations)
        if nb != 0:
            BU_Number_of_allocations_L.append(nb)

    BU_values.append(1.*sum(BU_Number_of_allocations_L)/len(BU_Number_of_allocations_L))


    TR_Number_of_allocations_L = list()
    for profile_A, profile_B in L_C:
        Allocations = TR(N=N, A_pprofile=profile_A, B_pprofile=profile_B)
        nb = len(Allocations)
        if nb != 0:
            TR_Number_of_allocations_L.append(nb)

    TR_values.append(1.*sum(TR_Number_of_allocations_L)/len(TR_Number_of_allocations_L))


os, = plt.plot(range(Nmin, Nmax+1, 2), OS_Number_of_allocations_L, color="blue")
rs, = plt.plot(range(Nmin, Nmax+1, 2), RS_Number_of_allocations_L, color="red")
tr, = plt.plot(range(Nmin, Nmax+1, 2), TR_Number_of_allocations_L, color="yellow")
bu, = plt.plot(range(Nmin, Nmax+1, 2), OS_Number_of_allocations_L, color="green")

plt.show()

#

# U = {i for i in range(1, N+1)}
# profile_A, profile_B = [1, 2, 3, 4], [2, 1, 3, 4]
# print(OS(A_pprofile=profile_A, B_pprofile=profile_B, U=U))
# U = {i for i in range(1, N+1)}
# print(OS(Alloc=list(), Z_A=set(), Z_B=set(),A_pprofile=profile_A, B_pprofile=profile_B, U=U))

# debug


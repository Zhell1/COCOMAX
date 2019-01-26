from algorithms import *
from cocomax import *
import time
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

Nmin = 4
Nmax = 12
print("Q1 : How many allocations are generated by each algorithm on average?")

#generation de couples de profils rapides jusqu'a N = 12
RS_values = list()
OS_values = list()
BU_values = list()
TR_values = list()


OS_frac_uniq = list()
RS_frac_uniq = list()
BU_frac_uniq = list()
TR_frac_uniq = list()



for N in range(Nmin, Nmax+1, 2):
    L_C = L_couple_single_peaked_preferences(N)
    print("Number of problems : {}".format(len(L_C)))



    OS_Number_of_allocations_L = list()
    os_n_frac_uniq = 0
    for profile_A, profile_B in L_C:
        U = {i for i in range(1, N+1)}
        Allocations = OS(Alloc=list(), Z_A=set(), Z_B=set(), A_pprofile=profile_A, B_pprofile=profile_B, U=U)
        nb_os = len(Allocations)
        if nb_os != 0:
            OS_Number_of_allocations_L.append(nb_os)
        if nb_os == 1:
            os_n_frac_uniq += 1

    OS_values.append(round(1.*sum(OS_Number_of_allocations_L)/len(OS_Number_of_allocations_L), 2))
    OS_frac_uniq.append(round(100.*os_n_frac_uniq/len(L_C), 1))

    RS_Number_of_allocations_L = list()
    rs_n_frac_uniq = 0
    for profile_A, profile_B in L_C:
        U = {i for i in range(1, N+1)}
        Allocations = RS(Alloc=list(), Z_A=set(), Z_B=set(), A_pprofile=profile_A, B_pprofile=profile_B, U=U)
        nb_rs = len(Allocations)
        if nb_rs != 0:
            RS_Number_of_allocations_L.append(nb_rs)
        if nb_rs == 1:
            rs_n_frac_uniq += 1

    RS_values.append(round(1.*sum(RS_Number_of_allocations_L)/len(RS_Number_of_allocations_L),2))
    RS_frac_uniq.append(round(100.*rs_n_frac_uniq/len(L_C), 1))

    BU_Number_of_allocations_L = list()
    bu_n_frac_uniq = 0
    for profile_A, profile_B in L_C:
        Allocations = BU(N=N, A_pprofile=profile_A, B_pprofile=profile_B)
        nb_bu = len(Allocations)
        if nb_bu != 0:
            BU_Number_of_allocations_L.append(nb_bu)
        if nb_bu == 1:
            bu_n_frac_uniq += 1

    BU_values.append(round(1.*sum(BU_Number_of_allocations_L)/len(BU_Number_of_allocations_L), 2))
    BU_frac_uniq.append(round(100.*bu_n_frac_uniq/len(L_C), 1))

    TR_Number_of_allocations_L = list()
    tr_n_frac_uniq = 0
    for profile_A, profile_B in L_C:
        Allocations = TR(N=N, A_pprofile=profile_A, B_pprofile=profile_B)
        nb_tr = len(Allocations)
        if nb_tr != 0:
            TR_Number_of_allocations_L.append(nb_tr)
        if nb_tr == 1:
            tr_n_frac_uniq += 1

    TR_values.append(round(1.*sum(TR_Number_of_allocations_L)/len(TR_Number_of_allocations_L), 2))
    TR_frac_uniq.append(round(100.*tr_n_frac_uniq/len(L_C), 1))


os, = plt.plot(range(Nmin, Nmax+1, 2), OS_values, color="blue")
rs, = plt.plot(range(Nmin, Nmax+1, 2), RS_values, color="red")
tr, = plt.plot(range(Nmin, Nmax+1, 2), TR_values, color="yellow")
bu, = plt.plot(range(Nmin, Nmax+1, 2), BU_values, color="green")


plt.legend([os, rs, tr, bu], ["OS : {}".format(OS_values), "RS : {}".format(RS_values), "TR : {}".format(TR_values), "BU : {}".format(BU_values)], loc = 'upper right',  markerscale = 100, frameon = False, fontsize = 10)
plt.title("Average number of allocations generated")
plt.savefig("Average_number_of_allocations_generated[{}].png".format(Nmax))
plt.close()

os1, = plt1.plot(range(Nmin, Nmax+1, 2), OS_frac_uniq, color="blue")
rs1, = plt1.plot(range(Nmin, Nmax+1, 2), RS_frac_uniq, color="red")
tr1, = plt1.plot(range(Nmin, Nmax+1, 2), TR_frac_uniq, color="yellow")
bu1, = plt1.plot(range(Nmin, Nmax+1, 2), BU_frac_uniq, color="green")


plt1.legend([os1, rs1, tr1, bu1], ["OS : {}".format(OS_frac_uniq), "RS : {}".format(RS_frac_uniq), "TR : {}".format(TR_frac_uniq), "BU : {}".format(BU_frac_uniq)], loc = 'upper right',  markerscale = 100, frameon = False, fontsize = 10)
plt1.title(" Fraction of problems in which a unique allocation is generated")
plt1.savefig(" Fraction_of_problems_in which_a_unique_allocation_is_generated[{}].png".format(Nmax))
plt1.close()

#

# U = {i for i in range(1, N+1)}
# profile_A, profile_B = [1, 2, 3, 4], [2, 1, 3, 4]
# print(OS(A_pprofile=profile_A, B_pprofile=profile_B, U=U))
# U = {i for i in range(1, N+1)}
# print(OS(Alloc=list(), Z_A=set(), Z_B=set(),A_pprofile=profile_A, B_pprofile=profile_B, U=U))

# debug


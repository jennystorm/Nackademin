# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:07:07 2023

@author: jenny
"""

# Övningsuppgift 2.1
citat = "datatyper har inbyggda metoder"
print (citat.upper())

# Övningsuppgift 2.2
x = float(input("Mata in ett flyttal:"))
print (round(x))

# Övningsuppgift 2.3
print("Hallå!")
f_name = input("Vad är ditt förnamn? ")
s_name = input("Vad är ditt efternamn? ")
print ("Trevligt att träffas", f_name, s_name +"!")

# Övningsuppgift 2.4
x = int(input("Hur gammal är du? "))
print ("Du är myndig om", 18-x, "år!")

# Övningsuppgift 2.5
a = 1
b = 9
c = 2
d = 6
e = 5
print (max(a, b, c, d, e))

# Övningsuppgift 2.6

import math

pris_va_korv = 20.95
pris_ve_korv = 34.95
pris_dryck = 13.95

va_korv_2 = int(input("Hur många ska äta 2 vanliga korvar?" ))
va_korv_3 = int(input("Hur många ska äta 3 vanliga korvar?" ))
ve_korv_2 = int(input("Hur många ska äta 2 veganska korvar?" ))
ve_korv_3 = int(input("Hur många ska äta 3 veganska korvar?" ))

elever = va_korv_2 + va_korv_3 + ve_korv_2 + ve_korv_3
antal_va_korv = va_korv_2*2 + va_korv_3*3
antal_ve_korv = ve_korv_2*2 + ve_korv_3*3

forp_va_korv = math.ceil(antal_va_korv/8)
forp_ve_korv = math.ceil(antal_ve_korv/4)

kostnad_va_korv = forp_va_korv * pris_va_korv
kostnad_ve_korv = forp_ve_korv * pris_ve_korv
kostnad_dryck = elever * pris_dryck

print ("Det behövs", forp_va_korv, "förpackningar vanlig korv. Det kostar", round(kostnad_va_korv, 2), "kr.")
print ("Det behövs", forp_ve_korv, "förpackningar vegansk korv. Det kostar", round(kostnad_ve_korv, 2), "kr.")
print ("Det behövs", elever, "stycken drycker. Det kostar", round(kostnad_dryck, 2), "kr.")
print ("Den totala kostnaden blir", kostnad_va_korv + kostnad_ve_korv + kostnad_dryck, "kr.")
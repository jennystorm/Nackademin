# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:37:12 2023

@author: jenny
"""


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

if antal_va_korv % 8 == 0:
    forp_va_korv = antal_va_korv/8
else:
    forp_va_korv = antal_va_korv/8 + 1 
    
if antal_ve_korv % 4 == 0:
    forp_ve_korv = antal_ve_korv/4
else:
    forp_ve_korv = antal_ve_korv/4 + 1

kostnad_va_korv = int(forp_va_korv) * pris_va_korv
kostnad_ve_korv = int(forp_ve_korv) * pris_ve_korv
kostnad_dryck = elever * pris_dryck

print ("Det behövs", int(forp_va_korv), "förpackningar vanlig korv. Det kostar", round(kostnad_va_korv, 2), "kr.")
print ("Det behövs", int(forp_ve_korv), "förpackningar vegansk korv. Det kostar", round(kostnad_ve_korv, 2), "kr.")
print ("Det behövs", elever, "stycken drycker. Det kostar", round(kostnad_dryck, 2), "kr.")
print ("Den totala kostnaden blir", kostnad_va_korv + kostnad_ve_korv + kostnad_dryck, "kr.")
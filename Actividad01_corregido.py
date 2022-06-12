# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:18:39 2022

@author: Dell
"""

def menu():
    print("1. DD a DMS ")
    print("2. DMS a DD")
    
def Conversion(numero):
   si_positivo = numero >= 0
   numero = abs(numero)
   minutes,seconds = divmod(numero*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if si_positivo else -degrees
   return (degrees,minutes,seconds);

def dms2dd(tup1):
    dd = float(tup1[0]) + float(tup1[1])/60 + float(tup1[2])/(60*60);
    return dd;

print("Selecciona el tipo de conversión que desea realizar: ");

menu()

option = int(input("Selecciona el numero: "))
 
while option != 0:
    if option == 1:
        numero = float(input("Escriba el valor de la Latitud en DD: "))
        print("La latitud es:");
        print(Conversion(numero));
    elif option == 2:
        dd = float(input("La Latitud en DD: "))
        print("La latitud es:");
        print(dms2dd(dd));
    else:
        print("Esa opcion no esta disponible.")

    menu()      

    option = int(input("Escriba su opcion: "))
 

import serial
import time
import os
arduino = serial.Serial('/dev/ttyACM0', 9600)
arduino.isOpen()

def Cocktail(mengen=[0,0,0,0,0,0,0,0,0,0], cocktail="unbekannt"):
    print("----------------------------------")
    print("Es wird gemixt: " + str(cocktail))
    
    
    for i in range(1,len(mengen)+1):
        if mengen[i-1] <= 0:
            continue
        print("Pumpe: " + str(i))
        befehl = str(i) + ',' + str(mengen[i-1]/2) + '\n'
        print(befehl)
        arduino.write(befehl.encode())
            
        print("fertig!")
  
werte = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pumpe = int(input("Pumpe: "))
menge = int(input("Menge [g]: "))
werte[pumpe-1] = menge
Cocktail(werte)
import serial
import time
import os
try:
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    print("/dev/ttyACM0")
except:
    arduino = serial.Serial('/dev/ttyACM1', 9600)
    print("/dev/ttyACM1")
    
arduino.isOpen()
os.system("clear")
cocktailgewicht = 170 #Gewicht eines jeden Cocktails

zeit = 5
for i in range(zeit, 0, -1):
    print("Inizialisiere (" + str(i) + "s)")
    time.sleep(1)
    os.system("cls")
global antwort

def Cocktail(mengen=[0,0,0,0,0,0,0,0,0,0], cocktail="unbekannt"):
    print("----------------------------------")
    print("Es wird gemixt: " + str(cocktail))
    
    befehl = ""
    gesamtgewicht = 0
    for g in mengen:
        gesamtgewicht = gesamtgewicht + g
        
    for i in range(1,len(mengen)+1):
        if i == len(mengen):
            print("Pumpe: " + str(i) + ", Menge: " + str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + "ml")
            befehl += str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + '\n'
            continue
        print("Pumpe: " + str(i) + ", Menge: " + str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + "ml")
        befehl += str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + ','
    print(befehl)
	
    arduino.write(befehl.encode())
    st = ""
    while True:
        ch = arduino.read().decode()
        if ch == "|":
            print(ch)
            break
        if (ch== "\n"):
            print (st)
            st = ""
            continue
        st += ch
    print("fertig!")

pumpe = 1
while True:
    werte = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pumpe = int(input("Pumpe: "))
    if pumpe < 1:
        break
    menge = int(input("Menge [g]: "))
    werte[pumpe-1] = menge
    Cocktail(werte)
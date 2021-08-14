# Getraenke in Reihenfolge: Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
import serial
import time
import os
try:
    arduino = serial.Serial('/dev/ttyACM1', 9600)
except:
    arduino = serial.Serial('/dev/ttyACM0', 9600)

arduino.isOpen()
cocktailgewicht = 100
for i in range(0, 4):
    print("Inizialisiere.")
    time.sleep(0.5)
    os.system("clear")
    print("Inizialisiere..")
    time.sleep(0.5)
    os.system("clear")
    print("Inizialisiere...")
    time.sleep(0.5)
    os.system("clear")
    
def Cocktail(mengen=[0,0,0,0,0,0,0,0,0,0], cocktail="unbekannt"):
    print("----------------------------------")
    print("Es wird gemixt: " + str(cocktail))
    
    gesamtgewicht = 0
    for g in mengen:
        gesamtgewicht = gesamtgewicht + g
    print(gesamtgewicht)
    
    for i in range(1,len(mengen)+1):
        if mengen[i-1] <= 0:
            continue
        print("Pumpe: " + str(i))
        befehl = str(i) + ',' + str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + '\n'
        print("Befehl: " + befehl)
        arduino.write(befehl)
        
        print("Verschluesselt: " + befehl)
        
        time.sleep(20)
        print("fertig!")
        
        
# Getraenke in Reihenfolge: Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup       
def eigener_cocktail():
    print("Nur ganze Zahlen sind zulaessig.\nDie Gesamtmenge darf 260 nicht ueberschreiten.")
    orange = int(input("Orangensaft [g]: "))
    grenadine = int(input("Grenadine [g]: "))
    zitrone = int(input("Zitronensaft [g]: "))
    ananas = int(input("Ananassaft [g]: "))
    maracuja = int(input("Maracujasaft [g]: "))
    sahne = int(input("Sahne [g]: "))
    grapefruit = int(input("Grapefruit[g]: "))
    limette = int(input("Limettensirup [g]: "))
    mango = int(input("Mangosirup [g]: "))
    kokos = int(input("Kokossirup [g]: "))

    
    if orange + grenadine + zitrone + ananas + maracuja + sahne + grapefruit + limette + mango + kokos > 260:
        print("Zu grosse Menge!")
        return
    Cocktail([orange, grenadine, zitrone, ananas, maracuja, sahne, grapefruit, limette, mango, kokos])
    
eigener_cocktail()

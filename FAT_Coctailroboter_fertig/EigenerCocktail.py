# Getraenke in Reihenfolge: Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
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
cocktailgewicht = 100 #Gewicht eines jeden Cocktails
zeit = 6
for i in range(zeit, 0, -1):
    print("Inizialisiere (" + str(i) + "s)")
    time.sleep(1)
    os.system("cls")
global antwort
# Getraenke in Reihenfolge: Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
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
            print("|")
            break
        if (ch== "\n"):
            print (st)
            st = ""
            continue
        st += ch
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

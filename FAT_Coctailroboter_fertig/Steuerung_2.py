from tkinter import *
import serial
import time
import os
import Cocktails
import _thread
from functools import partial

try:
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    print("/dev/ttyACM0")
except:
    arduino = serial.Serial('/dev/ttyACM1', 9600)
    print("/dev/ttyACM1")
    
arduino.isOpen()
os.system("clear")

cocktailgewicht = 180 #Gewicht eines jeden Cocktails
zeit = 6

for i in range(zeit, 0, -1):
    print("Inizialisiere (" + str(i) + "s)")
    time.sleep(1)
    os.system("cls")
    
# ist True wenn bereits ein Cocktail gemixt wird

    


# Getraenke in Reihenfolge: Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Cocktail(cocktail):
    
    print("Thread gestartet!")
    #return
    
    mengen = cocktail.getMengen()
    name = cocktail.getName()
    
    textfield.insert(INSERT,"Es wird gemixt: " + str(name) + "\n")
    
    befehl = ""
    gesamtgewicht = 0
    
    
    
    # addiert das Gewicht jeder Zutat zum Gesamtgewicht
    for gewicht in mengen:
        gesamtgewicht = gesamtgewicht + gewicht
    
    for pumpe in range(1,len(mengen)+1):
        # Gewicht des Cocktails (Prozentual auf "cocktailgewicht" hochgerechnet)
        menge = int((mengen[pumpe-1]/gesamtgewicht)*cocktailgewicht)
        
        #textfield.insert(INSERT,"Pumpe: " + str(pumpe) + ", Menge: " + str(menge) + "ml" + "\n")
        befehl += str(menge)
        
        if pumpe != len(mengen):
            befehl += ","
            continue
        befehl += "\n"
        
    print(befehl)

    arduino.write(befehl.encode())

    RasPiAusgabe = ""
    while True:
        arduinoAusgabe = arduino.read().decode()
        # "|" --> Endsignal
        if arduinoAusgabe == "|":
            print(arduinoAusgabe)
            break
        # Wenn Absatz --> RasPiAusgabe ausgeben und clearen
        if (arduinoAusgabe == "\n"):
            textfield.insert(INSERT,RasPiAusgabe + "\n")
            RasPiAusgabe = ""
            continue
        RasPiAusgabe += arduinoAusgabe
    
    textfield.insert(INSERT,cocktail.getBeschreibung() + "\n")
    textfield.insert(INSERT,"Genießen Sie ihr Getränk! :-D")
    mixt_aktuell = False
    
# Startet Methode "Cocktail" als eigenen Thread und gibts Namen in GUI aus
def startCocktail(cocktail):
    #if mixt_aktuell == True:
    #    print("Error: Es wird bereits ein Cocktail gemixt!")
    #    return
    #mixt_aktuell = True
    textfield.delete("1.0", END)
    _thread.start_new_thread(Cocktail, (cocktail, ))

#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
cocktails = [Cocktails.Cocktail("Sonnenaufgang","nichts",[150,22,10,0,0,0,0,0,0,0]),
             Cocktails.Cocktail("Tai_Fruit_Punch", "schuetteln",[50,12,10,40,50,0,0,0,0,0]),
             Cocktails.Cocktail("Bora_Bora","nichts",[0,12,10,100,60,0,0,0,0,0]),
             Cocktails.Cocktail("Catkisses","schuetteln",[40,0,0,100,0,20,0,0,0,22]),
             Cocktails.Cocktail("Fruit_Highball","Sodawasser und ruehren",[60,12,0,0,0,0,40,22,0,0]),
             Cocktails.Cocktail("Glacier_Express","schuetteln",[0,0,20,0,0,0,120,42,0,0]),
             Cocktails.Cocktail("California","schuetteln",[80,0,0,0,0,0,80,22,22,0]),
             Cocktails.Cocktail("Eros","ruehren",[40,0,0,40,40,0,40,0,22,0]),
             Cocktails.Cocktail("Exotic_Dream","schuettlen",[120,0,0,0,120,0,0,0,0,22]),
             Cocktails.Cocktail("Coco_Loco","schuetteln",[60,0,0,60,60,20,0,0,0,22]),
             Cocktails.Cocktail("Dream_of_Grenada","schuetteln",[0,22,0,120,0,40,0,0,0,22]),
             Cocktails.Cocktail("Pumpentest","Wat soll man da groß Zubereiten? Das testet doch nur die Pumpen!",[10,10,10,10,10,10,10,10,10,10])]
    
window = Tk()
window.config(bg = "white")

buttons = []
buttonframe = Frame(master = window)

for i in cocktails:
    buttons.append(Button(master = buttonframe,
                            text = i.getName(),
                            command = partial(startCocktail, i),
                            width = 15,
                            font = ("Arial",10),
                            fg = "black",
                            bg = "white"))

textfield = Text(master = window,
                    width = 50)

for button in buttons:
    button.pack()

buttonframe.pack(side = "left")

textfield.pack(side = "right")

window.mainloop()
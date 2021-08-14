from tkinter import *
import serial
import time
import os
import Cocktails

try:
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    print("/dev/ttyACM0")
except:
    arduino = serial.Serial('/dev/ttyACM1', 9600)
    print("/dev/ttyACM1")
    
arduino.isOpen()
os.system("clear")

cocktailgewicht = 10 #Gewicht eines jeden Cocktails
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
    
    # addiert das Gewicht jeder Zutat zum Gesamtgewicht
    for gewicht in mengen:
        gesamtgewicht = gesamtgewicht + gewicht
    
    for pumpe in range(1,len(mengen)+1):
        # Gewicht des Cocktails (Prozentual auf "cocktailgewicht" hochgerechnet)
        menge = int((mengen[pumpe-1]/gesamtgewicht)*cocktailgewicht)
        
        print("Pumpe: " + str(pumpe) + ", Menge: " + str(menge) + "ml")
        befehl += str(menge)
        
        if pumpe != len(mengen):
            befehl += ","
            continue
        befehl += "\n"
        
#        if pumpe == len(mengen):
#            print("Pumpe: " + str(pumpe) + ", Menge: " + str(int((mengen[pumpe-1]/gesamtgewicht)*cocktailgewicht)) + "ml")
#            befehl += str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + '\n'
#            continue
#        print("Pumpe: " + str(i) + ", Menge: " + str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + "ml")
#        befehl += str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + ','
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

#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Sonnenaufgang():
    Cocktail([150,22,10,0,0,0,0,0,0,0], "Sonnenaufgang")
    print("Zubereitung:")
    print("Sonnenaufgang: nichts")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Tai_Fruit_Punch():
    Cocktail([50,12,10,40,50,0,0,0,0,0], "Tai_Fruit_Punch")
    print("Zubereitung:")
    print("Tai_Fruit_Punch: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Bora_Bora():
    Cocktail([0,12,10,100,60,0,0,0,0,0], "Bora_Bora")
    print("Zubereitung:")
    print("Bora_Bora: nichts")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Catkisses():
    Cocktail([40,0,0,100,0,20,0,0,0,22], "Catkisses")
    print("Zubereitung:")
    print("Catkisses: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Fruit_Highball():
    Cocktail([60,12,0,0,0,0,40,22,0,0], "Fruit_Highball")
    print("Zubereitung:")
    print("Fruit_Highball: Sodawasser und ruehren")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Glacier_Express():
    Cocktail([0,0,20,0,0,0,120,42,0,0], "Glacier_Express")
    print("Zubereitung:")
    print("Glacier_Express: schuetteln")

#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Californian():
    Cocktail([80,0,0,0,0,0,80,22,22,0], "Californian")
    print("Zubereitung:")
    print("Californian: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Eros():
    Cocktail([40,0,0,40,40,0,40,0,22,0], "Eros")
    print("Zubereitung:")
    print("Eros: ruehren")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Exotic_Dream():
    Cocktail([120,0,0,0,120,0,0,0,0,22], "Exotic_Dream")
    print("Zubereitung:")
    print("Exotic_Dream: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Coco_Loco():
    Cocktail([60,0,0,60,60,20,0,0,0,22], "Coco_Loco")
    print("Zubereitung:")
    print("Coco_Loco: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Dream_of_Grenada():
    Cocktail([0,22,0,120,0,40,0,0,0,22], "Dream_of_Grenada")
    print("Zubereitung:")
    print("Dream_of_Grenada: schuetteln")
    
def Pumpentest():
    Cocktail([10,10,10,10,10,10,10,10,10,10], "Pumpentest")
    print("Zubereitung:")
    print("Pumpentest")    
    
window = Tk()
window.config(bg = "white")

btnSonnenaufgang = Button(master = window,
                          text = "Sonnenaufgang",
                          command = Sonnenaufgang,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnTai_Fruit_Punch = Button(master = window,
                          text = "Tai_Fruit_Punch",
                          command = Tai_Fruit_Punch,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnBora_Bora= Button(master = window,
                          text = "Bora_Bora",
                          command = Bora_Bora,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnCatkisses = Button(master = window,
                          text = "Catkisses",
                          command = Catkisses,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnFruit_Highball = Button(master = window,
                          text = "Fruit_Highball",
                          command = Fruit_Highball,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnGlacier_Express = Button(master = window,
                          text = "Glacier_Express",
                          command = Glacier_Express,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnCalifornian = Button(master = window,
                          text = "Californian",
                          command = Californian,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnEros = Button(master = window,
                          text = "Eros",
                          command = Eros,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnExotic_Dream = Button(master = window,
                          text = "Exotic_Dream",
                          command = Exotic_Dream,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnCoco_Loco = Button(master = window,
                          text = "Coco_Loco",
                          command = Coco_Loco,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnDream_of_Grenada = Button(master = window,
                          text = "Dream_of_Grenada",
                          command = Dream_of_Grenada,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")

btnPumpentest = Button(master = window,
                          text = "Pumpentest",
                          command = Pumpentest,
                          width = 15,
                          font = ("Arial",10), fg = "black", bg = "white")


btnSonnenaufgang.pack()
btnTai_Fruit_Punch.pack()
btnBora_Bora.pack()
btnCatkisses.pack()
btnFruit_Highball.pack()
btnGlacier_Express.pack()
btnCalifornian.pack()
btnEros.pack()
btnExotic_Dream.pack()
btnCoco_Loco.pack()
btnDream_of_Grenada.pack()
btnPumpentest.pack()


window.mainloop()
                  

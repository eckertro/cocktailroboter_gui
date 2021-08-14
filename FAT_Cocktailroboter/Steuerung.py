from tkinter import *
import serial
import time
import os
arduino = serial.Serial('/dev/ttyACM0', 9600)
arduino.isOpen()
os.system("clear")
cocktailgewicht = 100 #Gewicht eines jeden Cocktails
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
global antwort
# Getraenke in Reihenfolge: Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Cocktail(mengen=[0,0,0,0,0,0,0,0,0,0], cocktail="unbekannt"):
    print("----------------------------------")
    print("Es wird gemixt: " + str(cocktail))
    
    gesamtgewicht = 0
    for g in mengen:
        gesamtgewicht = gesamtgewicht + g
    
    for i in range(1,len(mengen)+1):
        if mengen[i-1] <= 0:
            continue
        print("Pumpe: " + str(i))
        befehl += str(i) + ',' + str(int((mengen[i-1]/gesamtgewicht)*cocktailgewicht)) + ','
        print(befehl)
	
	arduino.write(befehl.encode())
            
        print("fertig!")

#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Sonnenaufgang():
    Cocktail([150,22,10], "Sonnenaufgang")
    print("Sonnenaufgang: nichts")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Tai_Fruit_Punch():
    Cocktail([50,12,10,40,50], "Tai_Fruit_Punch")
    print("Tai_Fruit_Punch: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Bora_Bora():
    Cocktail([0,12,10,100,60], "Bora_Bora")
    print("Bora_Bora: nichts")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Catkisses():
    Cocktail([40,0,0,100,0,20,0,0,0,22], "Catkisses")
    print("Catkisses: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Fruit_Highball():
    Cocktail([60,12,0,0,0,0,40,22], "Fruit_Highball")
    print("Fruit_Highball: Sodawasser und ruehren")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Glacier_Express():
    Cocktail([0,0,20,0,0,0,120,42], "Glacier_Express")
    print("Glacier_Express: schuetteln")

#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Californian():
    Cocktail([80,0,0,0,0,0,80,22,22], "Californian")
    print("Californian: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Eros():
    Cocktail([40,0,0,40,40,0,40,0,22], "Eros")
    print("Eros: ruehren")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Exotic_Dream():
    Cocktail([120,0,0,0,120,0,0,0,0,22], "Exotic_Dream")
    print("Exotic_Dream: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Coco_Loco():
    Cocktail([60,0,0,60,60,20,0,0,0,22], "Coco_Loco")
    print("Coco_Loco: schuetteln")
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Dream_of_Grenada():
    Cocktail([0,22,0,120,0,40,0,0,0,22], "Dream_of_Grenada")
    print("Dream_of_Grenada: schuetteln")
    
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


window.mainloop()
                  

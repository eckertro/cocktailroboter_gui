from tkinter import *
import serial
import time
# Getränke in Reihenfolge: Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Cocktail(mengen=[0,0,0,0,0,0,0,0,0,0]):           
    global antwort
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    arduino.isOpen()
    time.sleep(5)
    #antwort = "1,10"
    #arduino.write(antwort.encode())
    for i in range(1,len(mengen)+1):
        if mengen[i-1] <= 0:
            continue
        print(i)
        befehl = str(i) + ',' + str(mengen[i-1]) + '\n'
        arduino.write(befehl.encode())
            
        print("fertig!")

#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Sonnenaufgang():
    Cocktail([150,20,10])

#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Tai_Fruit_Punch():
    Cocktail([50,10,10,40,50])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Bora_Bora():
    Cocktail([0,10,10,100,60])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Catkisses():
    Cocktail([40,0,0,100,0,20,0,0,0,20])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Fruit_Highball():
    Cocktail([60,10,0,0,0,0,40,20])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Glacier_Express():
    Cocktail([0,0,20,0,0,0,120,40])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Californian():
    Cocktail([80,0,0,0,0,0,80,20,20])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Eros():
    Cocktail([40,0,0,40,40,0,40,0,20])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Exotic_Dream():
    Cocktail([120,0,0,0,120,0,0,0,0,20])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Coco_Loco():
    Cocktail([60,0,0,60,60,20,0,0,0,20])
    
#Orangensaft, Grenadine, Zitronensaft, Ananassaft, Maracujasaft, Sahne, Grapefruit, Limettensirup, Mangosirup, Kokossirup
def Dream_of_Grenada():
    Cocktail([0,20,0,120,0,40,0,0,0,20])
    
    
window = Tk()

btnSonnenaufgang = Button(master = window,
                          text = "Sonnenaufgang",
                          command = Sonnenaufgang,
                          font = ("Arial",10), fg = "black")

btnTai_Fruit_Punch = Button(master = window,
                          text = "Tai_Fruit_Punch",
                          command = Tai_Fruit_Punch,
                          font = ("Arial",10), fg = "black")

btnBora_Bora= Button(master = window,
                          text = "Bora_Bora",
                          command = Bora_Bora,
                          font = ("Arial",10), fg = "black")

btnCatkisses = Button(master = window,
                          text = "Catkisses",
                          command = Catkisses,
                          font = ("Arial",10), fg = "black")

btnFruit_Highball = Button(master = window,
                          text = "Fruit_Highball",
                          command = Fruit_Highball,
                          font = ("Arial",10), fg = "black")

btnGlacier_Express = Button(master = window,
                          text = "Glacier_Express",
                          command = Glacier_Express,
                          font = ("Arial",10), fg = "black")

btnCalifornian = Button(master = window,
                          text = "Californian,
                          command = Californian,
                          font = ("Arial",10), fg = "black")

btnEros = Button(master = window,
                          text = "Eros",
                          command = Eros,
                          font = ("Arial",10), fg = "black")

btnExotic_Dream = Button(master = window,
                          text = "Exotic_Dream",
                          command = Exotic_Dream,
                          font = ("Arial",10), fg = "black")

btnCoco_Loco = Button(master = window,
                          text = "Coco_Loco",
                          command = Coco_Loco,
                          font = ("Arial",10), fg = "black")

btnDream_of_Grenada = Button(master = window,
                          text = "Dream_of_Grenada",
                          command = Dream_of_Grenada,
                          font = ("Arial",10), fg = "black")


btnSonnenaufgang.pack()

window.mainloop()
                  

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from tkinter import messagebox
from threading import Thread
from datetime import datetime
import matplotlib.pyplot as plt
from ultralytics import YOLO
import librosa
import librosa.display
from pathlib import Path 
from tkinter import filedialog
from playsound import playsound

def NEW():
   root = Tk()
   root.geometry("400x400")
   root.resizable(0,0)
   root.iconbitmap("drone.ico")
   root.title(" RECONNAISSANCE DU SON ")
   
   
   Message='''SYSTÈME DE RECONNAISSANCE DU SON



Ceci est un système de reconnaissance sonore développé par Aiman AL-FAHAD.
Cette application de reconnaissance sonore a été développée pour aider à sécuriser :
 


LES MARCHÉS:

CONVERTIR LE SON EN SPECTROGRAMME:

1-Cliquez En "Convertir Le Son En Spect" , prenez le Ton Du Fichier De Votre PC. 
2-La Tonalité Audio Sera Convertie En SPECTROGRAMME.

SON DE RECONNAISSANCE:
1-Cliquez En "CLASSIFICATION" , prenez le Ton Du Fichier De Votre PC. 
2- L'application classera les tonalités audio à l'aide d'un modèle "YOLO", 
et une nouvelle fenêtre apparaîtra avec deux options, la première option Est "Afficher" 
Le nom de la classe à laquelle appartient la tonalité n'est pas affiché, 	     
La deuxième option consiste à quitter la fenêtre actuelle.
			  
			  
  
		Aiman AL-FAHAD	  
			 
      '''  
   def Take_input():
       Output.insert(END, Message)
   inputtxt = Text(root, height = 1,
                width = 22,
                bg = "darkslategray3",bd=7)
   btn = Button(root, height = 1,bg="darkslategray3",
                 width = 22,
                 text ="Quitter",bd=7,
                 command = root.destroy)			
				
	
 
   Output = Text(root, height = 30,
              width = 50,
              bg = "light cyan")
 
   Display = Button(root, height = 1,bg="darkslategray3",
                 width = 22,
                 text ="Afficher",bd=7,
                 command = lambda:Take_input())

 
   # l.pack()
   btn.pack(padx=15, pady=5)
   btn.place(x=13,y=5)
   Display.pack(padx=15, pady=4)
   Display.place(x=210, y=4)
   Output.pack(padx=15, pady=60)
   
   mainloop()
   
def classif():
   root = Tk()
   root.geometry("400x400")
   root.resizable(0,0)
   root.iconbitmap("drone.ico")
   root.title(" RECONNAISSANCE DU SON ")
   
   im_ =' Mel Spectrogram.png'
   #print(im_)
 
   model = YOLO('last.pt')  # load a custom model
   results = model(im_)  # predict on an image
   names_dict = results[0].names
   probs = results[0].probs.tolist()
   #print(names_dict)
   #print(probs)
   numcl= names_dict[np.argmax(probs)]
   #print(numcl)
	

   def Take_input():
       Output.insert(END, numcl)
	   
   inputtxt = Text(root, height = 1,
                width = 22,
                bg = "light yellow",bd=7)
   btn = Button(root, height = 1,bg="darkslategray3",
                 width = 22,
                 text ="Quitter",bd=7,
                 command = root.destroy)			
				
	
 
   Output = Text(root, height = 30,
              width = 50,
              bg = "light cyan")
 
   Display = Button(root, height = 1,bg="darkslategray3",
                 width = 22,
                 text ="COMMENCER",bd=7,
                 command = lambda:Take_input())

 
   # l.pack()
   btn.pack(padx=15, pady=5)
   btn.place(x=13,y=5)
   Display.pack(padx=15, pady=4)
   Display.place(x=210, y=4)
   Output.pack(padx=15, pady=60)
   
   mainloop()   
   
   
   
   

def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("wav files",
														"*.wav*"),
													("all files",
														"*.*")))
	
	# Change label contents
	#label_file_explorer.configure(text="File Opened: "+filename)
	#print(filename)
	x = Path(filename).name
	#print(x)
	playsound(x)
	messagebox.showinfo("Reconnaissance sonore","Veuillez patienter quelques minutes......")
	y, sr = librosa.load(x)
	#print(sr)
	mel_spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=512  , n_mels=128)
	mel_spect = librosa.power_to_db(mel_spect, ref=np.max)
	librosa.display.specshow(mel_spect, y_axis='mel', fmax=8000, x_axis='time');
	plt.title('Mel Spectrogram');
	plt.colorbar(format='%+2.0f dB');
	plt.savefig( " Mel Spectrogram.png")
	if(True):
	  messagebox.showinfo("Reconnaissance sonore","La conversion est terminée.....")
	  



window = tk.Tk()
window.title("SYSTÈME DE RECONNAISSANCE DU SON")
window.resizable(0,0)
window.iconbitmap("drone.ico")

load1 = Image.open("DRONG.jpg")
photo1 = ImageTk.PhotoImage(load1)

header = tk.Button(window, image=photo1,bd=6)
header.place(x=5, y=0)


canvas0= Canvas(window, width= 400, height= 118, bg="darkturquoise")
canvas0.place(x=205, y=0)
canvas0.create_text(200, 50, text="SYSTÈME DE RECONNAISSANCE DU SON", fill="black", font=('Algerian',14))

canvas1 = Canvas(window, width = 400, height=200, bg='darkturquoise')
canvas1.place(x=5, y=120)
canvas1.create_text(151,20, text=" CONVERTIR LE SON EN SPECTROGRAMME ", fill="black", font=('Algerian',12))

canvas2 =  Canvas(window, width=400, height=580,bg='darkturquoise')
canvas2.place(x=5, y=300)
canvas2.create_text(102,20, text="SON DE RECONNAISSANCE  ", fill="black", font=('Algerian',12))

load11 = Image.open("DRON2.jpg")
photo11 = ImageTk.PhotoImage(load11)

aiman = tk.Button(window, image=photo11,bd=6)
aiman.place(x=407, y=120 ,width=200, height=179)

b3 = tk.Button(window, text="RENSEIGNEMENTS",width=17, height=9, font=("Algerian", 13), bg="darkslategray3", fg="black",bd=4,command=NEW)
b3.place(x=410, y=300 )

b2= tk.Button(canvas2, text="classification", font=("Algerian",16), bg='darkslategray3', fg='black',bd=10, command = classif)
b2.place(x=10, y=60,width=390,height=90)

b4 = tk.Button(canvas1, text="convertir le son en spect", font=("Algerian", 16), bg="darkslategray3", fg="black",bd=10, command=browseFiles)
b4.place(x=10, y=60,width=390,height=90)

window.geometry("590x490")
window.mainloop()
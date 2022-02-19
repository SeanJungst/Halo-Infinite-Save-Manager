import shutil
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from os.path import exists

def CreateWidgets():
	destinationLabel = Label(root, text ="Save Directory : ")
	destinationLabel.grid(row = 1, column = 0,
						pady = 5, padx = 5)
	
	root.destinationText = Entry(root, width = 50,
								textvariable = destinationLocation)
	root.destinationText.grid(row = 1, column = 1,
							pady = 5, padx = 5,
							columnspan = 2)
	
	dest_browseButton = Button(root, text ="Browse",
							command = DestinationBrowse, width = 15)
	dest_browseButton.grid(row = 1, column = 3,
						pady = 5, padx = 5)
	
	Gbraakon_Button = Button(root, text ="Warship Gbraakon",
						command = CopyGbraakon, width = 20)
	Gbraakon_Button.grid(row = 2, column = 1,
					pady = 5, padx = 5)

	Foundation_Button = Button(root, text ="Foundation",
						command = CopyFoundation, width = 20)
	Foundation_Button.grid(row = 2, column = 2,
					pady = 5, padx = 5)
	
	Tremonius_Button = Button(root, text ="Outpost Tremonius",
					command = CopyTremonius, width = 20)
	Tremonius_Button.grid(row = 3, column = 1,
					pady = 5, padx = 5)

	Golf_Button = Button(root, text ="FOB Golf",
					command = CopyGolf, width = 20)
	Golf_Button.grid(row = 3, column = 2,
					pady = 5, padx = 5)

	Tower_Button = Button(root, text ="The Tower",
					command = CopyTower, width = 20)
	Tower_Button.grid(row = 4, column = 1,
					pady = 5, padx = 5)

	Excavation_Button = Button(root, text ="Excavation Site",
					command = CopyExcavation, width = 20)
	Excavation_Button.grid(row = 4, column = 2,
					pady = 5, padx = 5)

	Conservatory_Button = Button(root, text ="Conservatory",
					command = CopyConservatory, width = 20)
	Conservatory_Button.grid(row = 5, column = 1,
					pady = 5, padx = 5)

	Spire_Button = Button(root, text ="Spire",
					command = CopySpire, width = 20)
	Spire_Button.grid(row = 5, column = 2,
					pady = 5, padx = 5)

	Pelican_Button = Button(root, text ="Pelican Down",
					command = CopyPelican, width = 20)
	Pelican_Button.grid(row = 6, column = 1,
					pady = 5, padx = 5)

	Sequence_Button = Button(root, text ="The Sequence",
					command = CopySequence, width = 20)
	Sequence_Button.grid(row = 6, column = 2,
					pady = 5, padx = 5)

	Nexus_Button = Button(root, text ="Nexus",
					command = CopyNexus, width = 20)
	Nexus_Button.grid(row = 7, column = 1,
					pady = 5, padx = 5)

	Command_Button = Button(root, text ="The Command Spire",
					command = CopyCommand, width = 20)
	Command_Button.grid(row = 7, column = 2,
					pady = 5, padx = 5)

	Repository_Button = Button(root, text ="Repository",
					command = CopyRepository, width = 20)
	Repository_Button.grid(row = 8, column = 1,
					pady = 5, padx = 5)

	Road_Button = Button(root, text ="The Road",
					command = CopyRoad, width = 20)
	Road_Button.grid(row = 8, column = 2,
					pady = 5, padx = 5)

	House_Button = Button(root, text ="House of Reckoning",
					command = CopyHouse, width = 20)
	House_Button.grid(row = 9, column = 1,
					pady = 5, padx = 5)

	Silent_Button = Button(root, text ="Silent Auditorium",
					command = CopySilent, width = 20)
	Silent_Button.grid(row = 9, column = 2,
					pady = 5, padx = 5)

	Extra1_Button = Button(root, text ="Additional Save One",
					command = CopyExtra1, width = 20)
	Extra1_Button.grid(row = 10, column = 1,
					pady = 5, padx = 5)

	Extra2_Button = Button(root, text ="Additional Save Two",
					command = CopyExtra2, width = 20)
	Extra2_Button.grid(row = 10, column = 2,
					pady = 5, padx = 5)

	destinationLabel = Label(root, text ="Created by @RealJadeBarker")
	destinationLabel.grid(row = 11, column = 0,
						pady = 5, padx = 5)

def InitialDirectory():
	return ".SaveDirectory/initialDirectory.txt"

def ReadDestinationLocation():
	if exists(InitialDirectory()):
		with open(InitialDirectory(), 'r') as file:
			init_dir = ""
			for line in file:
				init_dir = line
			destinationLocation.set(init_dir)	

def WriteDestinationLocation(destinationdirectory):
	with open(InitialDirectory(), 'w') as file:
		file.write(destinationdirectory)

def DestinationBrowse():
	previous_dir = destinationLocation
	destinationdirectory = filedialog.askdirectory(initialdir = "")
	if destinationdirectory != previous_dir.get() and destinationdirectory != "":
		root.destinationText.delete('0', 'end')
		root.destinationText.insert('1', destinationdirectory)
		WriteDestinationLocation(destinationdirectory)

def CopyGbraakon():
	Gbraakon_save = "./Warship Gbraakon/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Gbraakon_save, destination_location)
	messagebox.showinfo("Done")
	
def CopyFoundation():
	Foundation_save = "./Foundation/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Foundation_save, destination_location)
	messagebox.showinfo("Done")

def CopyTremonius():
	Tremonius_save = "./Outpost Tremonius/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Tremonius_save, destination_location)
	messagebox.showinfo("Done")
	
def CopyGolf():
	Golf_save = "./FOB Golf/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Golf_save, destination_location)
	messagebox.showinfo("Done")

def CopyTower():
	Tower_save = "./The Tower/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Tower_save, destination_location)
	messagebox.showinfo("Done")

def CopyExcavation():
	Excavation_save = "./Excavation Site/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Excavation_save, destination_location)
	messagebox.showinfo("Done")

def CopyConservatory():
	Conservatory_save = "./Conservatory/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Conservatory_save, destination_location)
	messagebox.showinfo("Done")

def CopySpire():
	Spire_save = "./Spire/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Spire_save, destination_location)
	messagebox.showinfo("Done")

def CopyPelican():
	Pelican_save = "./Pelican Down/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Pelican_save, destination_location)
	messagebox.showinfo("Done")

def CopySequence():
	Sequence_save = "./The Sequence/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Sequence_save, destination_location)
	messagebox.showinfo("Done")

def CopyNexus():
	Nexus_save = "./Nexus/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Nexus_save, destination_location)
	messagebox.showinfo("Done")

def CopyCommand():
	Command_save = "./The Command Spire/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Command_save, destination_location)
	messagebox.showinfo("Done")

def CopyRepository():
	Repository_save = "./Repository/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Repository_save, destination_location)
	messagebox.showinfo("Done")

def CopyRoad():
	Road_save = "./The Road/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Road_save, destination_location)
	messagebox.showinfo("Done")

def CopyHouse():
	House_save = "./House of Reckoning/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(House_save, destination_location)
	messagebox.showinfo("Done")

def CopySilent():
	Silent_save = "./Silent Auditorium/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Silent_save, destination_location)
	messagebox.showinfo("Done")

def CopyExtra1():
	Extra1_save = "./Extra 1/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Extra1_save, destination_location)
	messagebox.showinfo("Done")

def CopyExtra2():
	Extra2_save = "./Extra 2/progress2.cb2"
	destination_location = destinationLocation.get()
	shutil.copy(Extra2_save, destination_location)
	messagebox.showinfo("Done")

root = tk.Tk()
root.title('Halo Infinite Save Manager')
root.geometry('620x390+50+50')
root.iconbitmap('./Infinite.ico')
root.resizable(False, False)
destinationLocation = StringVar()
ReadDestinationLocation()

CreateWidgets()

root.mainloop()

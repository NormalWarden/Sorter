from os import listdir, mkdir
from pathlib import Path
from shutil import move
from tkinter import *
from tkinter import ttk, messagebox, filedialog

def sortAll():
	checkBox = [archiveCheck.get(),
				pictureCheck.get(),
				videoCheck.get(),
				documentCheck.get(),
				musicCheck.get(),
				appCheck.get(),
				torrentCheck.get(),
				scriptCheck.get()]
	try:
		path = filedialog.askdirectory() #main path
		content = listdir(path) #all files
		number = len(content) #count of files

		#check of folders
		for i in range(len(folders)):
			if (folders[i] in content) == False:
				mkdir(path + "\\" + folders[i])
			else:
				continue
				
		#sort
		for i in range(number):
			a = Path(path + content[i]).suffix
			src = path + '\\' + content[i]
			
			if a in archive:
				dst = path + '\\' + "Archives\\" + content[i]
				move(src, dst)

			elif a in picture:
				dst = path + '\\' + "Pictures\\" + content[i]
				move(src, dst)

			elif a in video:
				dst = path + '\\' + "Video\\" + content[i]
				move(src, dst)

			elif a in document:
				dst = path + '\\' + "Documents\\" + content[i]
				move(src, dst)

			elif a in music:
				dst = path + '\\' + "Music\\" + content[i]
				move(src, dst)

			elif a in app:
				dst = path + '\\' + "Programms\\" + content[i]
				move(src, dst)

			elif a in torrent:
				dst = path + '\\' + "Torrents\\" + content[i]
				move(src, dst)
			elif a in script:
				dst = path + '\\' + "Scripts\\" + content[i]
				move(src, dst)

			if i==number-1:
				messagebox.showinfo("End", 
					                "Sorting is complete, restart the programm for new sort")

	except FileNotFoundError:
		messagebox.showerror("Error", 
			                 "File not found")

def sortSelective():
	checkBox = [archiveCheck.get(),
				pictureCheck.get(),
				videoCheck.get(),
				documentCheck.get(),
				musicCheck.get(),
				appCheck.get(),
				torrentCheck.get(),
				scriptCheck.get()]

	if archiveCheck.get() == False:
		folders.pop(folders.index("Archives"))
	if pictureCheck.get() == False:
		folders.pop(folders.index("Pictures"))
	if videoCheck.get() == False:
		folders.pop(folders.index("Video"))
	if documentCheck.get() == False:
		folders.pop(folders.index("Documents"))
	if musicCheck.get() == False:
		folders.pop(folders.index("Music"))
	if appCheck.get() == False:
		folders.pop(folders.index("Programms"))
	if torrentCheck.get() == False:
		folders.pop(folders.index("Torrents"))
	if scriptCheck.get() == False:
		folders.pop(folders.index("Scripts"))
	try:
		path = filedialog.askdirectory() #main path
		content = listdir(path) #all files
		number = len(content) #count of files

		#check of folders
		for i in range(len(folders)):
			if (folders[i] in content) == False:
				mkdir(path + "\\" + folders[i])
			else:
				continue
				
		#sort
		for i in range(number):
			a = Path(path + content[i]).suffix
			src = path + '\\' + content[i]
			
			if a in archive and checkBox[0] == True:
				dst = path + '\\' + "Archives\\" + content[i]
				move(src, dst)

			elif a in picture and checkBox[1] == True:
				dst = path + '\\' + "Pictures\\" + content[i]
				move(src, dst)

			elif a in video and checkBox[2] == True:
				dst = path + '\\' + "Video\\" + content[i]
				move(src, dst)

			elif a in document and checkBox[3] == True:
				dst = path + '\\' + "Documents\\" + content[i]
				move(src, dst)

			elif a in music and checkBox[4] == True:
				dst = path + '\\' + "Music\\" + content[i]
				move(src, dst)

			elif a in app and checkBox[5] == True:
				dst = path + '\\' + "Programms\\" + content[i]
				move(src, dst)

			elif a in torrent and checkBox[6] == True:
				dst = path + '\\' + "Torrents\\" + content[i]
				move(src, dst)
			elif a in script and checkBox[7] == True:
				dst = path + '\\' + "Scripts\\" + content[i]
				move(src, dst)

			if i==number-1:
				messagebox.showinfo("End", 
					                "Sorting is complete, restart the programm for new sort")
	except FileNotFoundError:
		messagebox.showerror("Error", 
			                 "File not found")

#Initializing
root = Tk()
root.title("Sorter")
root.geometry("200x150")
root.iconbitmap("icon.ico")
archiveCheck = BooleanVar()
pictureCheck = BooleanVar()
videoCheck = BooleanVar()
documentCheck = BooleanVar()
musicCheck = BooleanVar()
appCheck = BooleanVar()
torrentCheck = BooleanVar()
scriptCheck = BooleanVar()
archiveCheck.set(0)
pictureCheck.set(0)
videoCheck.set(0)
documentCheck.set(0)
musicCheck.set(0)
appCheck.set(0)
torrentCheck.set(0)
scriptCheck.set(0)
btn1 = ttk.Button(text ="SORT ALL", 
	             style = "C.TButton", 
	             command = sortAll)
btn1.place(x=5, 
	      y=110)
btn2 = ttk.Button(text = "SELECTIVE SORT", 
	             style = "C.TButton", 
	             command = sortSelective)
btn2.place(x=100, 
	      y=110)

c1 = ttk.Checkbutton(text = "Archives", 
					 variable = archiveCheck, 
					 onvalue = 1, 
					 offvalue = 0)
c1.place(x = 5,
		 y = 10)
c2 = ttk.Checkbutton(text = "Pictures", 
					 variable = pictureCheck, 
					 onvalue = 1, 
					 offvalue = 0)
c2.place(x = 100,
		 y = 10)
c3 = ttk.Checkbutton(text = "Video", 
					 variable = videoCheck, 
					 onvalue = 1, 
					 offvalue = 0)
c3.place(x = 5,
		 y = 30)
c4 = ttk.Checkbutton(text = "Documents", 
					 variable = documentCheck, 
					 onvalue = 1, 
					 offvalue = 0)
c4.place(x = 100,
		 y = 30)
c5 = ttk.Checkbutton(text = "Music", 
					 variable = musicCheck, 
					 onvalue = 1, 
					 offvalue = 0)
c5.place(x = 5,
		 y = 50)
c6 = ttk.Checkbutton(text = "Programms", 
					 variable = appCheck, 
					 onvalue = 1, 
					 offvalue = 0)
c6.place(x = 100,
		 y = 50)
c7 = ttk.Checkbutton(text = "Torrents", 
					 variable = torrentCheck, 
					 onvalue = 1, 
					 offvalue = 0)
c7.place(x = 5,
		 y = 70)
c8 = ttk.Checkbutton(text = "Scripts", 
					 variable = scriptCheck, 
					 onvalue = 1, 
					 offvalue = 0)
c8.place(x = 100,
		 y = 70)

#Expansions
archive = [".rar", ".zip", ".7z", ".tar"]
picture = [".png", ".jpg", ".jpeg", ".gif", ".tif", ".bmp", ".ico", ".psd", ".tiff", ".svg", ".tga"]
video = [".mpeg", ".avi", ".mp4", ".mkv"]
document = [".doc", ".xls", ".txt", ".ppt", ".pdf"]
music = [".mp3", ".wav", ".mid", ".midi"]
app = [".exe", ".lnk"]
torrent = [".torrent"]
script = [".py", ".cpp", ".c", ".php", ".h", ".hpp", ".rb"]
folders = ["Archives", "Pictures", "Video", "Documents", "Music", "Programms", "Torrents", "Scripts"] #Folders for sort

root.resizable(False, False)
root.mainloop()  
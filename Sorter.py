from os import listdir
from pathlib import Path
from shutil import move
from tkinter import *
from tkinter import ttk, messagebox, filedialog

def sort():
	try:
		path = filedialog.askdirectory() #main path
		content = listdir(path) #all files
		number = len(content) #count of files

		#sort
		for i in range(number):
			a = Path(path + content[i]).suffix
			src = path + '\\' + content[i]
			
			#archive
			if a in archive:
				dst = path + '\\' + 'Archives\\' + content[i]
				move(src, dst)

			#image
			elif a in picture:
				dst = path + '\\' + 'Pictures\\' + content[i]
				move(src, dst)

			#video
			elif a in video:
				dst = path + '\\' + 'Video\\' + content[i]
				move(src, dst)

			#document
			elif a in document:
				dst = path + '\\' + 'Documents\\' + content[i]
				move(src, dst)

			#music
			elif a in music:
				dst = path + '\\' + 'Music\\' + content[i]
				move(src, dst)

			#app
			elif a in exe:
				dst = path + '\\' + 'Programms\\' + content[i]
				move(src, dst)

			#torrent
			elif a in torrent:
				dst = path + '\\' + 'Torrents\\' + content[i]
				move(src, dst)

			if i==number-1:
				messagebox.showinfo('End', 
					                'Sorting is complete')

	except FileNotFoundError:
		messagebox.showerror('Error', 
			                 'File not found')

#Initializing
root = Tk()
root.title('Sorter')
root.geometry('200x45')
root.iconbitmap('icon.ico')
messagebox.showinfo('Introduction', 
	                '1. Click BROWSE AND SORT \n 2. Choose folder \n 3. Ok')


btn = ttk.Button(text='BROWSE AND SORT', 
	             style="C.TButton", 
	             command=sort)
btn.place(x=43, 
	      y=10)

#Expansions
archive = ['.rar', '.zip']
picture = ['.png', '.jpg', '.jpeg', '.gif', '.tif', '.bmp', '.ico' ]
video = ['.mpeg', '.avi', '.mp4']
document = ['.doc', '.xls', '.txt', '.ppt', ]
music = ['.mp3']
exe = ['.exe', '.lnk']
torrent = ['.torrent']

root.mainloop()  
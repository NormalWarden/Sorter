#импорт всех библиотек
from os import listdir
from pathlib import Path
from shutil import move
from tkinter import *
from tkinter import ttk, messagebox, filedialog

#инициализация функций
def sort():
	try:
		path = filedialog.askdirectory() #путь
		content = listdir(path) #все файлы
		number = len(content) #количсетво файлов в папке

		#сортировка
		for i in range(number):
			a = Path(path + content[i]).suffix #расширение файла
			src = path + '\\' + content[i]
			
			#архив
			if a in archive:
				dst = path + '\\' + 'Archives\\' + content[i] #путь для архивов
				move(src, dst)
			#картинка
			elif a in picture:
				dst = path + '\\' + 'Pictures\\' + content[i] ##путь для картинок
				move(src, dst)

			#видео
			elif a in video:
				dst = path + '\\' + 'Video\\' + content[i] ##путь для видео
				move(src, dst)

			#текстовый документ
			elif a in document:
				dst = path + '\\' + 'Documents\\' + content[i] ##путь для документов
				move(src, dst)

			#музыка
			elif a in music:
				dst = path + '\\' + 'Music\\' + content[i] ##путь для музыки
				move(src, dst)

			#приложение
			elif a in exe:
				dst = path + '\\' + 'Programms\\' + content[i] ##путь для приложений
				move(src, dst)

			#торрент
			elif a in torrent:
				dst = path + '\\' + 'Torrents\\' + content[i] ##путь для торрент файлов
				move(src, dst)

			if i==number-1:
				messagebox.showinfo('Конец', 
					                'Сортировка выполнена')

	except FileNotFoundError:
		messagebox.showerror('Ошибка', 
			                 'Такого пути не существует')

#инициализация интерфейса
root = Tk()
root.title('Sorter')
root.geometry('200x45')
root.iconbitmap('icon.ico')
messagebox.showinfo('Ознакомление', 
	                'Для того, чтобы отсортировать папку вам нужно:\n 1. Нажать кнопку BROWSE AND SORT \n 2. Выбрать нужную папку \n 3. Нажать Ок')


btn = ttk.Button(text='BROWSE AND SORT', 
	             style="C.TButton", 
	             command=sort)
btn.place(x=43, 
	      y=10)

#расширения
archive = ['.rar', '.zip'] #расширения архива
picture = ['.png', '.jpg', '.jpeg', '.gif', '.tif', '.bmp', '.ico' ] #расширение картинки
video = ['.mpeg', '.avi', '.mp4'] #расширение видео
document = ['.doc', '.xls', '.txt', '.ppt', ] #расширения текстовых документов
music = ['.mp3'] #расширения музыки
exe = ['.exe', '.lnk'] #расширение приложения
torrent = ['.torrent'] #расширение для торрентов

root.mainloop()  
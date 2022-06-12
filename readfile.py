import pyttsx3
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fdg
import tkinter.messagebox as msg
import os
from threading import Thread

#My First Github Project

class App(tk.Tk):
	def __init__(self):
		super().__init__()


		self.title("File Reader")
		self.main_label = ttk.Label(self, text="A simple utility to read files").pack()
		self.file_box = tk.Listbox(self, width=30)
		self.file_box.pack()
		self.button_frame = tk.Frame(self).pack()
		self.file_btn = ttk.Button(self.button_frame, text="Add File", command=self.add_file)
		self.file_btn.focus()
		self.file_btn.pack()
		self.read_btn = ttk.Button(self.button_frame, state=tk.DISABLED, text="Read File", command=lambda:self.__thread_wrap(self.read_file(self.file)))
		self.read_btn.pack()

	def add_file(self):
		self.file = str(fdg.askopenfilename())
		self.file_name = os.path.basename(self.file)
		if bool(self.file):
			self.file_box.insert(tk.END, self.file_name)
			self.read_btn.config(state=tk.NORMAL)
		else:
			msg.showwarning("Error", "Please Select A File")

	def read_file(self, file):
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[2].id)
		with open(file) as f:
			lines = f.read()
			engine.setProperty('rate', 130)
			engine.say(lines)
			engine.runAndWait()

	def __thread_wrap(self, method):
		thread_method = Thread(target=method)
		thread_method.start()
if __name__ == '__main__':
	app = App()
	app.mainloop()

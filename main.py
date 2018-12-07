import tkinter
import resource


class MainWindow(tkinter.LabelFrame):
	def __init__(self, parent, **options):
		super(MainWindow, self).__init__(parent, **options)

		# Menu
		menu = tkinter.Menu(self)
		submenu = tkinter.Menu(menu)
		menu.add_cascade(label="menu", menu=submenu)
		submenu.add_command(label="label", command=lambda: print("submenu: label clicked"))
		submenu_cb_var = tkinter.BooleanVar(value=True)
		submenu.add_checkbutton(label="checkbutton", variable=submenu_cb_var, command=lambda: print("submenu: checkbutton = " + str(submenu_cb_var.get())))
		self.master.config(menu=menu)

		# Buttons
		btn_frame = tkinter.Frame(self)
		btn_frame.grid(column=0, row=0)
		btn1 = tkinter.Button(btn_frame, text="Button1", command=lambda: print("Button1: clicked"))
		btn1.grid(column=0, row=0)
		btn2 = tkinter.Button(btn_frame, text="Button2", command=lambda: print("Button2: clicked"))
		btn2.grid(column=0, row=1)
		btn3 = tkinter.Button(btn_frame, text="Button3", command=lambda: print("Button3: clicked"))
		btn3.grid(column=0, row=2)

		# Checkbuttons
		cb_frame = tkinter.Frame(self)
		cb_frame.grid(column=1, row=0)
		cb1_var = tkinter.BooleanVar(value=True)
		cb1 = tkinter.Checkbutton(cb_frame, text="Checkbutton1", variable=cb1_var, command=lambda: print("Checkbox1:" + str(cb1_var.get())))
		cb1.grid(column=0, row=0)
		cb2_var = tkinter.BooleanVar()
		cb2 = tkinter.Checkbutton(cb_frame, text="Checkbutton2", variable=cb2_var, command=lambda: print("Checkbox2:" + str(cb1_var.get())))
		cb2.grid(column=0, row=1)
		cb3_var = tkinter.BooleanVar()
		cb3 = tkinter.Checkbutton(cb_frame, text="Checkbutton3", variable=cb3_var, command=lambda: print("Checkbox3:" + str(cb1_var.get())))
		cb3.grid(column=0, row=3)

		# Radiobuttons
		rb_frame = tkinter.Frame(self)
		rb_frame.grid(column=2, row=0)
		self.rb_var = tkinter.IntVar(value=0)
		rb1 = tkinter.Radiobutton(rb_frame, text="Radiobutton1", variable=self.rb_var, value=0, command=lambda:print("rb1 selected"))
		rb1.grid(column=0, row=0)
		rb2 = tkinter.Radiobutton(rb_frame, text="Radiobutton2", variable=self.rb_var, value=1, command=lambda:print("rb2 selected"))
		rb2.grid(column=0, row=1)
		rb3 = tkinter.Radiobutton(rb_frame, text="Radiobutton3", variable=self.rb_var, value=2, command=lambda:print("rb3 selected"))
		rb3.grid(column=0, row=2)
		rb1.invoke()

		# Canvas
		canvas1 = tkinter.Canvas(self, width=100, height=50)
		canvas1.create_line(0, 0, 100, 50, fill="blue", dash=(4, 4))
		canvas1.create_line(0, 50, 100, 0, fill="red", dash=(4, 4))
		canvas1.create_text(50, 25, text="Canvas")
		canvas1.create_oval(5, 5, 100, 50)
		canvas1.grid(column=3, row=0)

		# Label
		label1 = tkinter.Label(self, text="Label")
		label1.grid(column=4, row=0)

		# Entry
		entry1_var = tkinter.StringVar(self, value='Entry')
		entry1 = tkinter.Entry(self, width=6, textvariable=entry1_var)
		entry1.grid(column=5, row=0)

		# Spinbox
		spinbox1_text = tkinter.StringVar(value="Spinbox")
		spinbox1 = tkinter.Spinbox(self, width=8, textvariable=spinbox1_text, command=lambda: print("Spinbox:up/down"))
		spinbox1.grid(column=6, row=0)

		# Scale
		scale1_var = tkinter.IntVar(value=50)
		scale1 = tkinter.Scale(self, label="Scale", variable=scale1_var, command=lambda x=str(scale1_var.get()): print("Scale:" + x))
		scale1.grid(column=7, row=0)

		# Listbox
		listbox1 = tkinter.Listbox(self, height=4)
		for i in range(5):
			listbox1.insert(i, "Listbox line " + str(i+1))
		listbox1.grid(column=8, row=0)

		# PhotoImage
		self.photo_image = tkinter.PhotoImage(data=resource.deer_img_b64)
		photo_label = tkinter.Label(self, image=self.photo_image)
		photo_label.grid(column=0, row=1, columnspan=3)

		# BitmapImage
		self.bitmap = tkinter.BitmapImage(data=resource.x11_bmp)
		bitmap_label = tkinter.Label(self, image=self.bitmap)
		bitmap_label.grid(column=3, row=1, columnspan=3)

		# Text + Scrollbar
		text = tkinter.Text(self, height=10, width=20)
		text.grid(column=6, row=1, columnspan=3, sticky='nsew')
		scrollbar1 = tkinter.Scrollbar(self, command=text.yview)
		scrollbar1.grid(row=1, column=9, sticky='nsew')
		text['yscrollcommand'] = scrollbar1.set
		text.insert("1.0", "Text + Scrollbar\n")
		text.insert("end", resource.lorem_ipsum_1000)

		# Add weight to all cells
		for x in range(10):
			tkinter.Grid.columnconfigure(self, 9, weight=1)
		for y in range(2):
			tkinter.Grid.rowconfigure(self, y, weight=1)

		# Add weight parent
		parent.columnconfigure(0, weight=1)
		parent.rowconfigure(0, weight=1)

		self.grid(column=0, row=0, sticky='nsew')


def main():
	root = tkinter.Tk()
	root.title("tk_all")
	main_window = MainWindow(root, text="Labelframe")
	root.mainloop()


if __name__ == "__main__":
	main()

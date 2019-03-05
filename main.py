import tkinter as tk
import tkinter.ttk as ttk
import resource


def bool_to_checked_str(value: bool) -> str:
	return "checked" if value else "unchecked"


class SelectWindow(ttk.Frame):
	def __init__(self, parent, **options):
		super(SelectWindow, self).__init__(parent, **options)
		self.parent = parent

		self.rb_var = tk.IntVar(value=0)
		rb1 = tk.Radiobutton(self, text="tk", variable=self.rb_var, value=0, command=self.rb_select)
		rb1.grid(column=0, row=0, sticky='nw')
		rb2 = tk.Radiobutton(self, text="themed tk", variable=self.rb_var, value=1, command=self.rb_select)
		rb2.grid(column=0, row=1, sticky='nw')

		self.style = ttk.Style()
		themes = self.style.theme_names()  # List of themes: https://wiki.tcl-lang.org/page/List+of+ttk+Themes

		self.themes_box = tk.Listbox(self, height=len(themes))

		for i, tn in enumerate(themes):
			self.themes_box.insert(i, tn)
		if len(themes) > 0:
			self.themes_box.select_set(0)
		self.themes_box.grid(column=0, row=2, sticky='nw')

		btn1 = tk.Button(self, text="Open", command=self.switch_window)
		self.themes_box.config(state="disabled")
		btn1.grid(column=0, row=3)

		self.grid(column=0, row=0, sticky='nsew')

	def rb_select(self):
		self.themes_box.config(state="normal" if self.rb_var.get() else "disabled")

	def switch_window(self):
		self.parent.withdraw()
		new_window = tk.Toplevel(self.parent)

		if self.rb_var.get():
			MainWindow.__bases__ = (ttk.Frame,)
			mw = MainWindow(new_window, self.parent)
			mw.style = self.style
			sel = self.themes_box.curselection()[0]
			print("Theme style {} selected - {}".format(sel, self.style.theme_names()[sel]))
			mw.style.theme_use(mw.style.theme_names()[sel])
		else:
			mw = MainWindow(new_window, self.parent)


class MainWindow(tk.Frame):
	def __init__(self, parent, root, **options):
		super(MainWindow, self).__init__(parent, **options)
		meta_menu = tk.Menu(self)

		parent.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.root = root

		# Menu1 (Labels)
		menu1 = tk.Menu(meta_menu, tearoff=False)
		meta_menu.add_cascade(label="Menu1", menu=menu1)
		menu1.add_command(label="Label1", command=lambda: print("Menu1: Label1 clicked"))
		menu1.add_command(label="Label2", command=lambda: print("Menu1: Label2 clicked"))
		menu1.add_command(label="Label3", command=lambda: print("Menu1: Label3 clicked"))

		# Menu2 (Checkbuttons)
		menu2 = tk.Menu(meta_menu)
		meta_menu.add_cascade(label="Menu2", menu=menu2)
		cb1_var = tk.BooleanVar(value=True)
		cb2_var = tk.BooleanVar()
		cb3_var = tk.BooleanVar()
		menu2.add_checkbutton(label="Checkbutton1", variable=cb1_var, command=lambda: print("Menu2: Checkbutton1 = " + bool_to_checked_str(cb1_var.get())))
		menu2.add_checkbutton(label="Checkbutton2", variable=cb2_var, command=lambda: print("Menu2: Checkbutton2 = " + bool_to_checked_str(cb2_var.get())))
		menu2.add_checkbutton(label="Checkbutton3", variable=cb3_var, command=lambda: print("Menu2: Checkbutton3 = " + bool_to_checked_str(cb3_var.get())))

		# Menu3 (Radiobuttons)
		menu3 = tk.Menu(meta_menu)
		meta_menu.add_cascade(label="Menu3", menu=menu3)
		self.rb_var = tk.IntVar(value=0)  # Self needed here to set a valid state.
		menu3.add_radiobutton(label="Radiobutton1", variable=self.rb_var, value=0, command=lambda: print("Menu3: Radiobutton1 selected"))
		menu3.add_radiobutton(label="Radiobutton2", variable=self.rb_var, value=1, command=lambda: print("Menu3: Radiobutton2 selected"))
		menu3.add_radiobutton(label="Radiobutton3", variable=self.rb_var, value=2, command=lambda: print("Menu3: Radiobutton3 selected"))

		self.master.config(menu=meta_menu)

		# Buttons
		btn_frame = tk.Frame(self)
		btn_frame.grid(column=0, row=0)
		btn1 = tk.Button(btn_frame, text="Button1", command=lambda: print("Button1: clicked"))
		btn1.grid(column=0, row=0)
		btn2 = tk.Button(btn_frame, text="Button2", command=lambda: print("Button2: clicked"))
		btn2.grid(column=0, row=1)
		btn3 = tk.Button(btn_frame, text="Button3", command=lambda: print("Button3: clicked"))
		btn3.grid(column=0, row=2)

		# Checkbuttons
		cb_frame = tk.Frame(self)
		cb_frame.grid(column=1, row=0)
		cb1 = tk.Checkbutton(cb_frame, text="Checkbutton1", variable=cb1_var, command=lambda: print("Checkbox1 = " + bool_to_checked_str(cb1_var.get())))
		cb1.grid(column=0, row=0)
		cb2 = tk.Checkbutton(cb_frame, text="Checkbutton2", variable=cb2_var, command=lambda: print("Checkbox2 = " + bool_to_checked_str(cb2_var.get())))
		cb2.grid(column=0, row=1)
		cb3 = tk.Checkbutton(cb_frame, text="Checkbutton3", variable=cb3_var, command=lambda: print("Checkbox3 = " + bool_to_checked_str(cb3_var.get())))
		cb3.grid(column=0, row=3)

		# Radiobuttons
		rb_frame = tk.Frame(self)
		rb_frame.grid(column=2, row=0)
		rb1 = tk.Radiobutton(rb_frame, text="Radiobutton1", variable=self.rb_var, value=0, command=lambda: print("Radiobutton1 selected"))
		rb1.grid(column=0, row=0)
		rb2 = tk.Radiobutton(rb_frame, text="Radiobutton2", variable=self.rb_var, value=1, command=lambda: print("Radiobutton2 selected"))
		rb2.grid(column=0, row=1)
		rb3 = tk.Radiobutton(rb_frame, text="Radiobutton3", variable=self.rb_var, value=2, command=lambda: print("Radiobutton3 selected"))
		rb3.grid(column=0, row=2)
		rb1.invoke()

		# Label
		label_frame = tk.Frame(self)
		label_frame.grid(column=3, row=0)
		label1 = tk.Label(label_frame, text="Label1")
		label1.grid(column=0, row=0)
		label2 = tk.Label(label_frame, text="Label2")
		label2.grid(column=0, row=1)
		label3 = tk.Label(label_frame, text="Label3")
		label3.grid(column=0, row=2)

		# Entry
		entry_frame = tk.Frame(self)
		entry_frame.grid(column=4, row=0)
		entry1_var = tk.StringVar(self, value='Entry1')
		entry1 = tk.Entry(entry_frame, width=6, textvariable=entry1_var)
		entry1.grid(column=0, row=0)
		entry2_var = tk.StringVar(entry_frame, value='Entry2')
		entry2 = tk.Entry(entry_frame, width=6, textvariable=entry2_var)
		entry2.grid(column=0, row=1)
		entry3_var = tk.StringVar(entry_frame, value='Entry3')
		entry3 = tk.Entry(entry_frame, width=6, textvariable=entry3_var)
		entry3.grid(column=0, row=2)

		# Spinbox
		spinbox_frame = tk.Frame(self)
		spinbox_frame.grid(column=5, row=0)
		spinbox1_text = tk.StringVar(value="Spinbox")
		spinbox1 = tk.Spinbox(spinbox_frame, width=8, textvariable=spinbox1_text, command=lambda: print("Spinbox:up/down"))
		spinbox1.grid(column=0, row=0)
		spinbox2 = tk.Spinbox(spinbox_frame, width=8, justify="center", from_=-10, to=10, command=lambda: print("Spinbox:up/down"))
		spinbox2.grid(column=0, row=1)
		spinbox3 = tk.Spinbox(spinbox_frame, width=8, justify="center", from_=1000, to=2500, increment=100, command=lambda: print("Spinbox:up/down"))
		spinbox3.grid(column=0, row=2)

		# Listbox
		listbox1 = tk.Listbox(self, height=4)
		for i in range(5):
			listbox1.insert(i, "Listbox line " + str(i + 1))
		listbox1.grid(column=6, row=0)

		# Scale
		scale1_var = tk.IntVar(value=50)
		scale1 = tk.Scale(self, label="Scale", variable=scale1_var, orient="horizontal", command=lambda x=str(scale1_var.get()): print("Scale:" + x))
		scale1.grid(column=7, row=0)

		# Canvas
		canvas1 = tk.Canvas(self, width=100, height=50)
		canvas1.create_line(0, 0, 100, 50, fill="blue", dash=(4, 4))
		canvas1.create_line(0, 50, 100, 0, fill="red", dash=(4, 4))
		canvas1.create_text(50, 25, text="Canvas")
		canvas1.create_oval(5, 5, 100, 50)
		canvas1.grid(column=8, row=0)

		# PhotoImage
		self.photo_image = tk.PhotoImage(data=resource.deer_img_b64)
		photo_label = tk.Label(self, image=self.photo_image)
		photo_label.grid(column=0, row=1, columnspan=3)

		# BitmapImage
		self.bitmap = tk.BitmapImage(data=resource.x11_bmp)
		bitmap_label = tk.Label(self, image=self.bitmap)
		bitmap_label.grid(column=3, row=1, columnspan=4)

		# Text + Scrollbar
		text = tk.Text(self, height=10, width=20)
		text.grid(column=7, row=1, columnspan=3, sticky='nsew')
		scrollbar1 = tk.Scrollbar(self, command=text.yview)
		scrollbar1.grid(row=1, column=9, sticky='nsew')
		text['yscrollcommand'] = scrollbar1.set
		text.insert("1.0", "Text + Scrollbar\n")
		text.insert("end", resource.lorem_ipsum_1000)

		# Add weight to all cells
		for x in range(10):
			tk.Grid.columnconfigure(self, x, weight=1)
		for y in range(2):
			tk.Grid.rowconfigure(self, y, weight=1)

		# Add weight to parent
		parent.columnconfigure(0, weight=1)
		parent.rowconfigure(0, weight=1)

		self.grid(column=0, row=0, sticky='nsew')

	def on_closing(self):
		print("on_closing")
		self.root.destroy()



def main():
	root = tk.Tk()
	root.title("tk_all")
	main_window = SelectWindow(root)#, text="Labelframe (w/ Grid)")
	root.mainloop()


if __name__ == "__main__":
	main()

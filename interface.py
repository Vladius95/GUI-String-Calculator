import tkinter as tk


class Application:
	def __init__(self):
		pass

	def bind_commands(self, cms, key, params=None):
		self._root.bind('<{}>'.format(key), lambda event: cms() if params is None else cms(*params))

	class Main:
		def __init__(self, root, width=640, height=420, title='Application', resizable=True):
			self._root = root
			self._root.geometry('{}x{}'.format(width, height))
			self._root.title(title)
			if not resizable:
				self._root.resizable(False, False)

		def bind_commands(self, cms, key='Key', params=None):
			assert key is not str, '"key" must be string type'
			self._root.bind('<{}>'.format(key), lambda event: cms() if params is None else cms(*params))

	class FieldEntry:
		keys_symbols = [i for i in range(24, 36)] + [i for i in range(38, 49)] + [i for i in range(51, 62)]

		def __init__(self, root, width, height, width_widget=300):
			self._enter = tk.Entry(root)
			self._enter.place(x=65, y=35, width=300)
			self._ban_symbols = None
			self._legal_symbols = None

		def add_text(self, text):
			self._enter.insert(tk.END, text)
			
		def _control_ban_symbols(self, event):
			symbol = event.char
 
			if event.keycode not in self.keys_symbols:
				pass
			elif symbol in self._ban_symbols:
				self.step_back()

		def _control_legal_symbols(self, event):
			symbol = event.char

			if event.keycode not in self.keys_symbols:
				pass
			elif symbol not in self._legal_symbols:
				self.step_back()

		def set_ban_symbols(self, *symbols):
			self._ban_symbols = symbols
			self._enter.bind('<Any-KeyRelease>', self._control_ban_symbols)

		def set_legal_symbols(self, *symbols):
			self._legal_symbols = symbols
			self._enter.bind('<Any-KeyRelease>', self._control_legal_symbols)

		def get_text(self):
			return self._enter.get()

		def step_back(self):
			self._enter.delete(len(self._enter.get())-1)

		def clear_input(self):
			self._enter.delete(0, tk.END)

		def bind_commands(self, cms, key='Key', params=None):
			assert key is not str, '"key" must be string type'
			self._enter.bind('<{}>'.format(key), lambda event: lambda: cms() if params is None else cms(*params))

	class FieldLabel:
		def __init__(self, root, width, height, label='label'):
			self._lbl_ans = tk.Label(root, text=label)
			self._lbl_ans.place(x=width, y=height)

		def set_text(self, new_text):
			self._lbl_ans.config(text=new_text)

	class Buttons:
		def __init__(self, root):
			self._root = root

		def create_button(self, text_button, x, y, width_button=5, enabled=tk.NORMAL, cms=None, params=None):
			btn = tk.Button(self._root, text=text_button, command=lambda: cms() if params is None else cms(*params), state=enabled, width=width_button)
			btn.place(x=x, y=y)
			return btn

		def turn_on_buttons(self, *buttons):
			for button in buttons:
				button.config(state=tk.NORMAL)

		def turn_off_buttons(self, *buttons):
			for button in buttons:
				button.config(state=tk.DISABLED)
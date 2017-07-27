import computing
import calculate_errors
from tkinter import messagebox

class Functional:
	def __init__(self):
		self.ans = 0

	def calculate(self, input_, output_frame):
		try:
			replace = {'!': 'fac'}
			
			string = []
			digit = []

			if ',' in input_:
				input_ = input_.replace(',', '.')

			for i in list(input_):

				if i.isalnum() or i == '.' or (len(digit) == 0 and i == '-'):
					digit.append(i)
				elif i in replace.keys():
					string.append(replace[i])
					string.append('(')
					string.append(''.join(digit))
					string.append(')')
					digit.clear()
				else:
					if digit or i == ')':
						string.append(''.join(digit))
						string.append(i)
						digit.clear()
					else:
						string.append(i)
			if digit:
				string.append(''.join(digit))
		
			result = computing.compute(string)
			self.ans = result
			output_frame('Result: '+result)
		except ZeroDivisionError as e_zero:
			messagebox.showinfo('Error', str(e_zero).capitalize()+'!!')
		except calculate_errors.NotEnclosedError as e_bracket:
			messagebox.showinfo('Error', e_bracket.message)
		except calculate_errors.SignError as e_sign:
			messagebox.showinfo('Error', e_sign.message)
		except calculate_errors.FunctionError as e_func:
			messagebox.showinfo('Error', e_func.message)
		except calculate_errors.ValueFuncError as e_val:
			messagebox.showinfo('Error', e_val.message)
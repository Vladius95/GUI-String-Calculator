import tkinter as tk
from interface import Application
from functional import Functional

def main():
	root = tk.Tk()
	app = Application()
	main = app.Main(root, 540, 380, 'String calculator', False)
	input_ = app.FieldEntry(root, 65, 35, 300)
	output = app.FieldLabel(root, 70, 70, 'Result: ')
	f = Functional()
	#/////////////////////////create buttons////////////////////////////////////////////////
	#/////////////////////////////digits///////////////////////////////////////////////////////
	btns = app.Buttons(root)
	commands = lambda text: (input_.add_text(text), btns.turn_on_buttons(btn_del, btn_clr, btn_calc))

	btn_7 = btns.create_button(text_button='7', x=50, y=100, width_button=1, cms=commands, params=('7',))

	btn_8 = btns.create_button(text_button='8', x=90, y=100, width_button=1, cms=commands, params=('8',))

	btn_9 = btns.create_button(text_button='9', x=130, y=100, width_button=1, cms=commands, params=('9',))

	btn_4 = btns.create_button(text_button='4', x=50, y=135, width_button=1, cms=commands, params=('4',))

	btn_5 = btns.create_button(text_button='5', x=90, y=135, width_button=1, cms=commands, params=('5',))

	btn_6 = btns.create_button(text_button='6', x=130, y=135, width_button=1, cms=commands, params=('6',))

	btn_1 =btns.create_button(text_button='1', x=50, y=170, width_button=1, cms=commands, params=('1',))

	btn_2 = btns.create_button(text_button='2', x=90, y=170, width_button=1, cms=commands, params=('2',))

	btn_3 = btns.create_button(text_button='3', x=130, y=170, width_button=1, cms=commands, params=('3',))

	btn_0 = btns.create_button(text_button='0', x=50, y=205, width_button=1, cms=commands, params=('0',))

	btn_i = btns.create_button(text_button='i', x=50, y=240, width_button=1, cms=commands, params=('i',))

	btn_pi = btns.create_button(text_button='pi', x=90, y=240, width_button=1, cms=commands, params=('pi',))

	btn_e = btns.create_button(text_button='e', x=130, y=240, width_button=1, cms=commands, params=('e',))
	#////////////////////////////signs/////////////////////////////////////////////////////////
	btn_plus = btns.create_button(text_button='+', x=210, y=100, width_button=1, cms=commands, params=('+',))

	btn_minus = btns.create_button(text_button='-', x=250, y=100, width_button=1, cms=commands, params=('-',))

	btn_mul = btns.create_button(text_button='*', x=210, y=135, width_button=1, cms=commands, params=('*',))

	btn_div = btns.create_button(text_button='/', x=250, y=135, width_button=1, cms=commands, params=('/',))

	btn_bracket_left = btns.create_button(text_button='(', x=210, y=170, width_button=1, cms=commands, params=('(',))

	btn_bracket_right = btns.create_button(text_button=')', x=250, y=170, width_button=1, cms=commands, params=(')',))

	btn_sqrt = btns.create_button(text_button='\u221A', x=210, y=205, width_button=1, cms=commands, params=('sqrt(',))

	btn_pow = btns.create_button(text_button='^', x=250, y=205, width_button=1, cms=commands, params=('^',))

	btn_comma = btns.create_button(text_button=',', x=90, y=205, width_button=1, cms=commands, params=(',',))

	btn_fac = btns.create_button(text_button='!', x=210, y=240, width_button=1, cms=commands, params=('!',))
	#///////////////////////////////functions/////////////////////////////////////////////////////
	btn_log2 = btns.create_button(text_button='log2(x)', x=320, y=100, cms=commands, params=('log2(',))

	btn_log10 = btns.create_button(text_button='log10(x)', x=320, y=140, cms=commands, params=('log10(',))

	btn_ln = btns.create_button(text_button='ln(x)', x=320, y=180, cms=commands, params=('ln(',))

	btn_exp = btns.create_button(text_button='exp(x)', x=390, y=100, cms=commands, params=('exp(',))

	btn_sin = btns.create_button(text_button='sin(x)', x=390, y=140, cms=commands, params=('sin(',))

	btn_cos = btns.create_button(text_button='cos(x)', x=390, y=180, cms=commands, params=('cos(',))

	btn_tan = btns.create_button(text_button='tan(x)', x=390, y=220, cms=commands, params=('tan(',))
	#////////////////////////////////////////////////others////////////////////////////////////////////////////////////////////
	commands_calc = lambda : (f.calculate(input_.get_text(), output.set_text), btns.turn_on_buttons(btn_ans, btn_clr, btn_del))
	btn_calc = btns.create_button(text_button='Calculate', x=375, y=55, width_button=7, enabled=tk.DISABLED, cms=commands_calc)
	
	commands_del = lambda : input_.step_back() if len(input_.get_text()) > 1 else (input_.step_back(),  btns.turn_off_buttons(btn_del, btn_clr, btn_calc))
	btn_del = btns.create_button(text_button='Delete', x=375, y=5, width_button=7, enabled=tk.DISABLED, cms=commands_del)

	commands_clr = lambda : (input_.clear_input(), btns.turn_off_buttons(btn_del, btn_clr, btn_calc))
	btn_clr = btns.create_button(text_button='Clear', x=375, y=30, width_button=7, enabled=tk.DISABLED, cms=commands_clr)

	commands_ans = lambda : (input_.add_text(f.ans), btns.turn_on_buttons(btn_del)) 
	btn_ans = btns.create_button(text_button='Ans', x=130, y=205, width_button=1, enabled=tk.DISABLED, cms=commands_ans)
	#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	input_command = lambda : btns.turn_on_buttons(btn_clr, btn_del, btn_calc)
	input_.bind_commands(input_command)

	main_commands = commands_calc
	main.bind_commands(main_commands, 'Return')

	signs = ['+', '-', '*', '/', '^', '(', ')', '!', ',', '.', 'e', 'x', 'p',
					'l', 'o', 'n', 'g', 's', 'q', 'r', 't', 'i', 'c', 'e', 'a']
	signs.extend([str(i) for i in range(10)])
	input_.set_legal_symbols(*signs)
	
	root.mainloop()

if __name__ == '__main__':
	main()
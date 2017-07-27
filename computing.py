import operator
import math
import calculate_errors

def scrape(number):
    start_len = len(number)
    for i in list(range(10)):
        temp = number.rstrip(str(i)).rstrip('.')
        if len(temp) < start_len:
            if temp == '-0':
                temp = '0'
            return temp
    return number

def output_format(number):
    assert number is not str, 'number must be string'

    output = 0
    if type(number) is int:
        output = str(number)

    elif type(number) is float:
        output = scrape('{0:.4f}'.format(number)).replace('.', ',')

    elif type(number) is complex:
        if number.imag == 0:
            if type(number.real) is float: 
                output = scrape('{0:.4f}'.format(number.real)).replace('.', ',')
            else:
                output = str(number.real)
        elif number.real == 0:
            if type(number.imag) is float: 
                output = scrape('{0:.4f}'.format(number.imag)).replace('.', ',')+'*i'
            else:
                output = str(number.imag).replace('j', '*i')
        else:
            re = scrape('{0:.4f}'.format(number.real)).replace('.', ',') if type(number.real) is float else str(number.real)
            sign = '-' if number.imag < 0 else '+'
            im = scrape('{0:.4f}'.format(abs(number.imag))).replace('.', ',') if type(number.imag) is float else str(abs(number.imag))

            output = '({}{}{}*i)'.format(re, sign, im)
    return output

def compute(string=['5', '+', '1']):
    signs = ('+', '-', '*', '/', '^')
    CONSTANTS = {'e': math.e, 'pi': math.pi}
    stack = []
    enter = []
    temp_str = []
    
    for i in string:
        if i.isdigit() or '.' in i or i == 'i' or ('-' in i and i[1:].isdigit()):
            enter.append(i)
        elif i in CONSTANTS:
            enter.append(str(CONSTANTS[i]))
        elif i.isalnum():
            temp_str.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            try:
                while stack[-1] != '(':
                    enter.append(stack.pop())
            except IndexError:
                raise calculate_errors.NotEnclosedError
            stack.pop()
            if len(temp_str) > 0:
                enter.append(temp_str.pop())
                
        elif i in signs:
            tmp = len(stack)
            if i in ('+', '-') and tmp>=1:
                while len(stack)>0 and stack[-1] in ('*', '/', '+', '-', '^'):
                    enter.append(stack.pop())
                    
            if i in ('*', '/') and tmp>=1:
                while len(stack)>0 and stack[-1] in ('*', '/', '^'):
                    enter.append(stack.pop())
                    
            if i == '^' and tmp>=1:
                while len(stack)>0 and stack[-1] == '^':
                    enter.append(stack.pop())
                    
            stack.append(i)

    while len(stack) != 0:
        enter.append(stack.pop())

    
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                 '/': operator.truediv, '^': operator.pow}
    FUNCTIONS = {'exp': math.exp, 'ln': math.log, 'log10': math.log10,
                 'log2': math.log2, 'sin': math.sin, 'cos': math.cos,
                 'tan': math.tan, 'sqrt': math.sqrt, 'fac': math.factorial}

    for token in enter:
    
        if token in OPERATORS:
            try:
                second = stack.pop()
                first = stack.pop()
                stack.append(OPERATORS[token](first, second))
            except IndexError:
                raise calculate_errors.SignError
            
        elif token in FUNCTIONS.keys():
            try:
                tmp = stack.pop()
                stack.append(FUNCTIONS[token](tmp))
            except ValueError:
                raise calculate_errors.ValueFuncError
        elif '.' in token:
            stack.append(float(token))
        
        elif token == 'i':
            stack.append(complex(0, 1))

        else:
            try:
                if len(token) > 1 and (not token.isdigit() and token[0] != '-'):
                    raise calculate_errors.FunctionError
                stack.append(int(token))
            except ValueError:
                raise calculate_errors.NotEnclosedError

    return output_format(stack.pop())

#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def do_twice(fName, value):
	fName(value)
	fName(value)

def print_twice(vString):
	print(vString)

def print_twice_inline(vString):
	print(vString, end = ' ')

def do_four(fName, value):
	do_twice(fName, value)
	do_twice(fName, value)

def print_2x2():
	# print('+', do_four(print_twice_inline, '- '), end = ' ')
	# print('+', do_four(print_twice_inline, '- '), end = ' ')
	# print('+', do_four(print_twice_inline, '- '), end = ' ')
	# print('+', do_four(print_twice_inline, '- '), end = ' ')
	# print('+')
	# do_four(print_twice_inline, '|         ')
	# do_four(print_twice_inline, '|         ')
	# do_four(print_twice_inline, '|         ')
	# do_four(print_twice_inline, '|         ')

	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+')
	print('|         |         |')
	print('|         |         |')
	print('|         |         |')
	print('|         |         |')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+')
	print('|         |         |')
	print('|         |         |')
	print('|         |         |')
	print('|         |         |')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+')

def print_4x4():
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')	
	print('+')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')	
	print('+')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')	
	print('+')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')	
	print('+')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('|         |         |         |         |')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')
	print('+', '- - - -', end=' ')	
	print('+')

# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    
    print()

    print_2x2()

    print()

    print_4x4()

if __name__ == "__main__":
    main()
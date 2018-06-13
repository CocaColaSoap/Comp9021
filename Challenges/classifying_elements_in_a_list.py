'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 99, prints out the list,
computes the number of elements equal to 0, 1, 2 3 modulo 4, and prints those out.
'''


from random import seed, randrange
import sys


# Prompts the user for a seed for the random number generator,
# and for a strictly positive number, nb_of_elements.
arg_for_seed = input('Input a seed for the random number generator: ')
try:
    arg_for_seed = int(arg_for_seed)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
# Generates a list of nb_of_elements random integers between 0 and 99.
seed(arg_for_seed)
L = [randrange(100) for _ in range(nb_of_elements)]
print('\nThe list is:' , L)
print()
# - remainders_modulo_4[0] to record the number of elements equal to 0 modulo 4,
# - remainders_modulo_4[1] to record the number of elements equal to 1 modulo 4,
# - remainders_modulo_4[2] to record the number of elements equal to 2 modulo 4,
# - remainders_modulo_4[3] to record the number of elements equal to 3 modulo 4.
remainders_modulo_4 = [0] * 4
for i in range(nb_of_elements):
    remainders_modulo_4[L[i] % 4] += 1
for i in range(4):
    if remainders_modulo_4[i] == 0:
        print('There is no element', end = ' ')
    elif remainders_modulo_4[i] == 1:
        print('There is 1 element', end = ' ')
    else:
        print(f'There are {remainders_modulo_4[i]} elements', end = ' ')
    print(f'equal to {i} modulo 4.')

print()

'''
Computes the number of elements strictly less 5, 10, 15 and 20, and prints those out.
'''


# Replace this comment with your code
L = [randrange(20) for _ in range(nb_of_elements)]
print('\nThe list is:' , L)
print()
reminders_count = [0] * 4
for i in range(nb_of_elements):
	if(L[i]<5):
		reminders_count[0] += 1
	elif(5<=L[i]<10):
		reminders_count[1] += 1
	elif(10<=L[i]<15):
		reminders_count[2] += 1
	else:
		reminders_count[3] += 1
for i in range(4):
    if reminders_count[i] == 0:
        print('There is no element', end = ' ')
    elif reminders_count[i] == 1:
        print('There is 1 element', end = ' ')
    else:
        print(f'There are {reminders_count[i]} elements', end = ' ')
    print(f'between {i*5} and {(i+1)*5-1}.')
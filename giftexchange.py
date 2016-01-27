import random

'''
NU CSA eBoard x EC 
Yankee Swap 2015
'''

people = ['Eric', 'Brian', 'Jess', \
'Michael', 'James', 'Julia', 'Maggie', \
'April', 'Hannah', 'Brandon', 'Alice', \
'Linda', 'Dixon', 'Dennis', 'Aaron', 'Lillian']

random.shuffle(people)

while people:
	current = people.pop()
	stalling = input('Press enter for the next person:')
	print('\n', current, '\n')

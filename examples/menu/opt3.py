#!/usr/bin/env python
import subprocess

short_name = 'Opt 3'
disp_name = 'Option 3 Submenu'
otype = 'Routine'
need = ['need 1: ', 'need 2: ', 'need 3: ']
answers = []

def run():
	global answers
	while True:
		subprocess.call('clear')
		i = 0
		while i < len(need):
			ans = input(need[i])

			if validate(ans):
				answers.append(ans)
				i += 1

		final = 'Doing something with '
		for a in answers:
			final = '{}, {}'.format(final, a)
		print(final)
		input()
		return

def validate(char):
	if char:
		return True
	return False
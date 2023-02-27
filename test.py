import os
from pymol import cmd

path = '/home2/satvik/JAK2-JH2/CRESSET/6D2I-JAK2JH2-D058-2-newpocket-growing/starter1/plain'

for file in os.listdir(path):
	file_n = os.path.splitext(file)[0]
	cmd.load(f'{path}/{file}')
	cmd.group(f'{file_n}', '*')
	cmd.save(f'{path}/{file}', f'{file_n}', 'state=0')

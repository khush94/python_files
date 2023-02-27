import os
from pymol import cmd

path = '/home2/satvik/JAK2-JH2/CRESSET/6D2I-JAK2JH2-D058-2-newpocket-growing/starter1/JAK2JH2_D058_growing_starter1_FDA-fragments-complex-plip-ind'

for file in os.listdir(path):
	file_n = os.path.splitext(file)[0]
	rep = file_n.replace("_PROTEIN_UNK_Z_900","_g")
	cmd.load(f'{path}/{file}')
	cmd.group(f'{rep}', '*')
	cmd.save(f'{path}/{file}', f'{rep}', 'state=0')

import os
from pymol import cmd

path = '/home2/satvik/JAK2-JH2/CRESSET/6D2I-JAK2JH2-D058-2-newpocket-growing/starter1/plain'
for file in os.listdir(path):
  file_n = os.path.splitext(file)[0]
  cmd.load(f'{path}/{file}')
  cmd.set_view ("""\
    -0.800359368,    0.472988844,   -0.368384838,\
    -0.061954033,   -0.676425993,   -0.733898282,\
    -0.596311450,   -0.564559460,    0.570688486,\
     0.000114053,    0.000138059,  -73.918678284,\
   -16.413455963,    6.903835297,  155.029647827,\
    57.755805969,   93.639244080,  -20.000000000 """)
  cmd.png(f'{path}/{file}.png', '10in', '10in', 300, 1)   	
  cmd.save(f'{path}/{file}.pse')
    	




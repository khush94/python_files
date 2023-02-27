import os
from pymol import cmd
from pymol import util

path = '/home2/satvik/JAK2-JH2/CRESSET/6D2I-JAK2JH2-D058-2-newpocket-growing/starter1/JAK2JH2_D058_growing_starter1_FDA-fragments-complex-plip-ind'

for file in os.listdir(path):
  file_n = os.path.splitext(file)[0]
  rep = file_n.replace("_PROTEIN_UNK_Z_900","_g")
  cmd.load(f'{path}/{file}')
  cmd.group(f'{rep}', '*')
  cmd.set_view ("""\
    -0.800359368,    0.472988844,   -0.368384838,\
    -0.061954033,   -0.676425993,   -0.733898282,\
    -0.596311450,   -0.564559460,    0.570688486,\
     0.000114053,    0.000138059,  -73.918678284,\
   -16.413455963,    6.903835297,  155.029647827,\
    57.755805969,   93.639244080,  -20.000000000 """)
  cmd.set('dash_gap', '0.4')
  cmd.set('dash_color', 'black', 'Hydrophobic')
  #cmd.set('dash_color', 'dgreen', 'PiStackingT')
  #cmd.set('dash_color', 'hotpink', 'Saltbridges')
  cmd.set('label_position', '(1.1,1.0,0.0)')
  cmd.set('label_color', '[0.0 , 0.0 , 0.0]')
  cmd.set('label_size', '7')
  cmd.hide('everything', 'ele h')
  cmd.show('sticks', 'ele h and neighbor (ele n+o)')
  cmd.select('resname UNK')
  util.cbag('sele')
  cmd.select('resn5', '((br. all within 5 of resn UNK) and (not resn UNK))')
  util.cbas('resn5')
  cmd.show('lines', 'resn5')
  cmd.remove('h. and (e. c extend 1)')
  one_letter = {'VAL':'VAL', 'ILE':'ILE', 'LEU':'LEU', 'GLU':'GLU', 'GLN':'GLN', \
  'ASP':'ASP', 'ASN':'ASN', 'HIS':'HIS', 'TRP':'TRP', 'PHE':'PHE', 'TYR':'TYR',    \
  'ARG':'ARG', 'LYS':'LYS', 'SER':'SER', 'THR':'THR', 'MET':'MET', 'ALA':'ALA',    \
  'GLY':'GLY', 'PRO':'PRO', 'CYS':'CYS'}
  cmd.select('resn5_ca', 'bca. resn5')
  cmd.label('resn5_ca', '"%s %s" % (resn,resi)')
  cmd.save(f'{path}/{file}')
  #cmd.png(f'{path}/{rep}.png', '10in', '10in', 300, 0, 0)

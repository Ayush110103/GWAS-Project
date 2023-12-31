# -*- coding: utf-8 -*-
"""SNP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EMNBJsCDldXR5CNH-1Q1lefO9JT1u8U0

Question 1
"""



import os

# Load the SNP matrix data in VCF format
os.system('bcftools view input.vcf.gz -Ou > output.bcf')

# Convert the SNP matrix data to ATGC format
os.system('bcftools query -f "%CHROM\\t%POS\\t%REF\\t%ALT[\\t%GT]\\n" output.bcf | sed "s/\\t[0-9|]\\+:[0-9|]\\+//g" | sed "s/\\t\\.\\t\\./\\tN\\tN/g" > output.tsv')

with open('output.tsv', 'r') as f:
    for line in f:
        print(line.strip())

#!/usr/bin/env python3

#
# h5m2csv.py: Convert HDF5 SNP matrix to CSV
#
# (c) 2021 by Joffrey Fitz (joffrey.fitz@tuebingen.mpg.de),
# Max Planck Institute for Developmental Biology,
# Tuebingen, Germany
#

import h5py, numpy
import pandas as pd
import numpy as np

f = h5py.File('/content/drive/MyDrive/GENOTYPES/4.hdf5','r')

# Get all SNP positions for all chromosomes (len=10709949)
positions = f['positions'][:]

# Array of tupels with start/stop indices for each chromosome
chr_regions = f['positions'].attrs['chr_regions']

# Array of SNP positions for all chromosomes, each chromosome is a hash
# with "Chr<N>" as key, and a numpy.array of positions as value.
snp_pos_on_chrs = [
	{ "label": "Chr1", "chr_idx": 0, "positions": positions[chr_regions[0][0]:chr_regions[0][1]] },
	{ "label": "Chr2", "chr_idx": 1, "positions": positions[chr_regions[1][0]:chr_regions[1][1]] },
	{ "label": "Chr3", "chr_idx": 2, "positions": positions[chr_regions[2][0]:chr_regions[2][1]] },
	{ "label": "Chr4", "chr_idx": 3, "positions": positions[chr_regions[3][0]:chr_regions[3][1]] },
	{ "label": "Chr5", "chr_idx": 4, "positions": positions[chr_regions[4][0]:chr_regions[4][1]] }
]

# Print header

f['positions'].attrs['chr_regions']

(f["accessions"])

(f["snps"])

f.keys()

x=list(f['positions'][:100])

z=list(f["accessions"])

y=list(f["snps"][:100])

print(list (f["snps"][1]))

dataset = pd.DataFrame({"pos": x})

print(list(y[0]))

df = pd.DataFrame(y, columns=z)
# df.head
df.insert(0, "Pos", x, False)
df.head

print(list(df[b'5916']))

df.to_csv('filo.csv')
# dataset.columns=z
df.head

from google.colab import drive
drive.mount('/content/drive')

print("#Chromosome", "Positon", "Count_zeros", "Count_ones"
	, ",".join(f['accessions'][:].astype(str)), sep=" " )
c=0
chro=[]
sn=[]
position=[]
label=[]
# Loop over all chromosomes

for chr in snp_pos_on_chrs:
	c=0
	# chro.append(chr)
  # snp.append([])
	# Loop over all positions
	for pos in numpy.nditer(chr["positions"]):
		c+=1




		ix= numpy.where(chr["positions"] == pos)[0][0]
		print(ix)
		# Add chromosome start position to SNP position
		ix = ix + chr_regions[chr["chr_idx"]][0]
		print(ix)

		# Get the corresponding SNPs for that position
		snps = f['snps'][ix]
    # snp.append(snps)
		# Count 0s in snps
		cnt_zeros = numpy.count_nonzero(snps==0)

		# Count 1s in snp
		cnt_ones = numpy.count_nonzero(snps==1)

		label.append(chr["label"])

	  # sn.append(snps)
	  # position.append(pos)
		# print(chr["label"], pos, cnt_zeros, cnt_ones
		# 	, ",".join(snps.astype(str)), sep=",")



# dict = {'chromosome': chro, 'snp': sn, 'position': position}
# df = pd.DataFrame(dict)
# df.to_csv('file1.csv')
# df.to_csv(r'C:\Users\Admin\Desktop\file3.csv')
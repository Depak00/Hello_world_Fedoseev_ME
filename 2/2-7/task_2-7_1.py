#!/bin/python
files = ["seq1", "seq2", "seq3", "seq4"]
data = ("26.02.2026")
for name in files:
   new_name = name + "_" + data + ".fasta"
   print(f"{new_name}")

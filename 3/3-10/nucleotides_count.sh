#!/bin/bash
echo "Файл A T G C"
for file in *.fasta; do
    [ -e "$file" ] || continue
    [ -s "$file" ] || continue
    a=$(grep -o 'A' "$file" | wc -l)
    t=$(grep -o 'T' "$file" | wc -l)
    g=$(grep -o 'G' "$file" | wc -l)
    c=$(grep -o 'C' "$file" | wc -l)
    echo "$file $a $t $g $c"
done

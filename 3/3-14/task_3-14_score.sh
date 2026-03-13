#!/bin/bash
awk '$2 > 80 {print $1, $2}' students.txt
awk '$2 < 70 {print $1, $2}' students.txt

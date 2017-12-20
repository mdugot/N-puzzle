#!/bin/bash

size="500"
for i in `seq 0 $size`
do
	echo $i / $size
	python npuzzle-gen.py -i $(( 1 + RANDOM% 50)) 3 > tmp ; (echo 1; echo n) | python3 main.py tmp | grep "heuristic cost" | tr -d "[]" | cut  -d " " -f1-9,15-16 | cat >> training_data_small
done

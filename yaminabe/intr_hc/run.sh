#!/bin/bash
echo "start compile..." &&
g++ A.cpp -o my_solution &&
echo "compile ok" &&
echo -n > result.txt &&
for ((i=0; i<10; i++)); do
    python3 tester/generator.py $RANDOM > input.txt &&
    ./my_solution < input.txt > output.txt &&
    python3 tester/tester.py input.txt output.txt | awk '(NR==2){print $2}' >> result.txt
done
cat result.txt | awk '{sum+=$1} END {print sum}'

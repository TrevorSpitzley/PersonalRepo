#! /bin/bash

sum=0
for i in $@
do
    (( sum+=$i ))
    shift
done

echo The sum is $sum

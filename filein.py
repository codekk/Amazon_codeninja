import sys
import fileinput
array=[]
for line in fileinput.input():
    element=(line.split())
    array.append(element)

print array    
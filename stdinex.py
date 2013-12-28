from StringIO import StringIO
from array import array
import sys

# fake stdin
std=sys.stdin.readline()

a = array('i')
a = [map(int, row.split()) for row in std]

print a

for i in range(0,len(a)):
    
    print a[i]
    print "\n"
    
print a[2]    
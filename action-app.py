import sys

try:
    p = float(sys.argv[1])
except ValueError:
    p = sys.argv[1]
    
print(p * 2)

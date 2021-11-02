import sys
import requests

filename = sys.argv[1]

with open(filename) as file:
    for line in file:
        filtered_line = line.rstrip()
        
        
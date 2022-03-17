#!/usr/bin/env python3

from hashlib import md5
from string import ascii_lowercase
import itertools

counter = 1
while True:
     combinations = itertools.product(ascii_lowercase, repeat=counter)

     for combo in combinations:
         string = "".join(combo)

         m = md5(string.encode("utf-8"))
         the_hash = m.hexdigest()
         if the_hash.endswith("001"):
             print(string, the_hash)
             exit()
     
     counter += 1
      
'''
Generate MD5 hashes until one ends with "001". 
Note: itertools.product(ascii_lowercase, repeat=counter) can be considered equivalent to a nested for-loop.
'''

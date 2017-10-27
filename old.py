#! /usr/bin/env python3
import sys


print("Goodbye")
print("Enter some numbers")
print("d)))

ut_of = int(sys.argv[1])



while 1:
    line = input()
    total = 0
    for num in line.split(" "):
        total += float(num)
    print("Total: %d (%f%%)" % (total, total * (100.0 / out_of)))


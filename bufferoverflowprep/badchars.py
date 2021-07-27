from __future__ import print_function

for x in range(1, 256):
  print("\\x" + "{:02x}".format(x), end='')
print()

""" listRem = "\\x07\\x2e\\xa0".split("\\x")
for x in range(1, 256):
    if "{:02x}".format(x) not in listRem:
        print("\\x" + "{:02x}".format(x), end='')
print() """
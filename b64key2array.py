import binascii
import base64
n=0
key = input("please enter your b64key ")
name = input("please enter key name ")
elements = base64.standard_b64decode(key)

# Create immutable bytes object.
data = bytes(elements)

# Loop over bytes.
for d in data:
    inp=str(d)
    medium=inp.replace("255","byte.MaxValue")
    out=name + "[" + str(n) + "] = " + medium + ";"
    print(out)
    n+=1

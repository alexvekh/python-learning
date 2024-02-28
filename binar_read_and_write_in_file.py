
def read():
    with open("b.jpg", "r+b") as f:
        b = f.read()
        return b
        #print(b)


def write():
    with open("b2.jpg", "a+b") as f:
        #b = b'\\xea\\x17UR\\xeaHC\\x08.L\\x11\\x1a`\\xc8'
        f.write("=================================================================================")

b = read()
print(b)
write()

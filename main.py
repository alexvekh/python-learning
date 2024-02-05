import sys


def parse_args():
    result = ""
    sys.argv.pop(0)     # delete [0]
    is_1_arg = True
    for arg in sys.argv:
        if is_1_arg:
            is_1_arg = False
            result = result + arg
        else:
            result = result + " " + arg    
    
    return result
print(parse_args())
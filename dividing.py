pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except TypeError:
    print('Wrong number')
except ZeroDivisionError:
    print('Not a zero!')
else:
     print(chunk, 'SMS in one package.')
import fibo

print('\n --> '
      'Modules Tutorial from '
      'https://docs.python.org/2/tutorial/modules.html'
      '\n')
# module = file name without '.py'
# parameter from print() changed - end= ' '
print('Accessing functions fib(n) and fib2(n) from fibo.py')
fibo.fib(100)
# Pycharm shortcut alt+1 to show/close project files tab
print('\n', fibo.fib2(100))
print("Printing the module's name form the global variable __name__:\n",
      fibo.__name__)
print('If you intend to use a function often you can assign it to a local name:\n'
      'fib = fibo.fib then just call it as fib(500) for example')
fib = fibo.fib
print(fib(500))


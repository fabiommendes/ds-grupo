def fib(n):
    """
    Imprime os n primeiros números de Fibonacci.
    """
    x, y = 1, 1
    
    for i in range(n):
        print(x)
        x, y = y, x + y
     
   

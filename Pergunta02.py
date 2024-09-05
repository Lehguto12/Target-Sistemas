def is_in_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    if a == n:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Insira um número: "))
print(is_in_fibonacci(numero))
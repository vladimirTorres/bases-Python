# def fibonacci(n):
#     print(n)
#     if n == 0 or n == 1:
#         return 1
    
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Escribe un numero: "))
# print (fibonacci(n))


# Pares
lista = list(range(100))
double = [i * 2 for i in lista]
pares = [i for i in lista if i % 2 == 0]

print(lista)
print("************************************")
print(double)
print("************************************")
print(pares)
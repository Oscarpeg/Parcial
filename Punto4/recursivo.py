import time
import tracemalloc  

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 900


start_time = time.time()
tracemalloc.start()  

resultado = factorial(num)

current, peak = tracemalloc.get_traced_memory()  
tracemalloc.stop()  
end_time = time.time()

print(f"Factorial({num}) = {resultado}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Memoria usada: {peak / 1024:.2f} KB")

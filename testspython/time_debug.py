import time
def fibRecursivo(num):
         # Por teoria si es 0 o 1,su fibonacci es 0 o 1 respectivamente
        if(num < 2):
                return num
        # Sino, se calcula sumando el fibonacci de los dos numeros anteriores recursivamente
        else:
                return (fibRecursivo(num-2) + fibRecursivo(num-1))
_num = int(input("Numero a calcular recursivo: "))
print(fibRecursivo(_num))
for i in range(_num):
        # time.time()
        # time.perf_counter()
        # time.process_time()
        inicio = time.time()
        fibRecursivo(i)
        fin = time.time()       
        # Presicion de 20 digitos
        print("tiempo de ",i,"%.20f"%(fin - inicio))





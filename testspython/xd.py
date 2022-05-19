def fibRecursivo(num):
    # Por teoria si es 0 o 1,su fibonacci es 0 o 1 respectivamente
    if(num < 2):
        return num
    # Sino, se calcula sumando el fibonacci de los dos numeros anteriores recursivamente
    else:
        return (fibRecursivo(num-2) + fibRecursivo(num-1))
listay = []
for i in range(0,20):
    listay.append(fibRecursivo(i+1))
print(listay)
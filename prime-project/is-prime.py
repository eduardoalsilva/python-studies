try:
    number = int(input())
    
except:
    print('Por favor entre com um numero')
    exit()
    
multiples = []
for i in range(1,number + 1):
    if number < 2:
        print('O numero deve ser maior que 1')
        exit()
        
    multiple = number % i == 0
    multiples.append(multiple)
    
prime = sum(multiples) == 2
print(f'{number} é primo? {prime}')
try:
    number = int(input())
    
except:
    print(f'{number} is not a number!')
    exit()
    
if number < 2:
    print('The number must be greater than 1')
    exit()
    
multiples = [number % i == 0 for i in range(1, number + 1)]

prime = sum(multiples) == 2
print(f'Is {number} a prime? {prime}')
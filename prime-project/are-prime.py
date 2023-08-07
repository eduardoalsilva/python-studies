#create a list of number and test if each of them are prime. Make a dictionary of it

def is_prime(number):
    multiples = [number % multiple == 0 for multiple in range(1,number + 1)]
    return sum(multiples) == 2

try:
    numbers = list(map(int, input().split()))
    
except:
    print('They must be only integers.')
    exit()
print(numbers)

are_prime = {number: is_prime(number) for number in numbers}

print(are_prime)